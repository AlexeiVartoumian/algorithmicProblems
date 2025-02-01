package main

import (
	"compress/gzip"
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"strings"
	"sync"
	"time"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/s3"
	"github.com/aws/aws-sdk-go-v2/service/s3/types"
)

type UserIdentity struct {
	Type           string         `json:"type"`
	UserName       string         `json:"userName,omitempty"`
	PrincipalId    string         `json:"principalId"`
	Arn            string         `json:"arn"`
	SessionContext SessionContext `json:"sessionContext,omitempty"`
	InvokedBy      string         `json:"invokedBy,omitempty"`
}
type SessionContext struct {
	SessionIssuer SessionIssuer `json:"sessionIssuer"`
}

type SessionIssuer struct {
	Type        string `json:"type"`
	UserName    string `json:"userName,omitempty"`
	PrincipalId string `json:"principalId"`
}

type Event struct {
	EventTime       string       `json:"eventTime"`
	EventName       string       `json:"eventName"`
	UserIdentity    UserIdentity `json:"userIdentity"`
	SourceIPAddress string       `json:"sourceIPAddress"`
}

type CloudTrailLog struct {
	Records []Event `json:"Records"`
}

type MatchedEvent struct {
	Timestamp       string
	Action          string
	User            string
	PrincipalId     string
	SourceIPAddress string
	Arn             string
	SessionIssuer   SessionIssuer
	InvokedBy       string
	SourceFile      string // Added this field
}

type FoundUser struct {
	UserName    string
	TotalEvents int
	Events      []MatchedEvent
}

type FoundUsers map[string]*FoundUser

// S3 processing types
type S3Processor struct {
	client      *s3.Client
	bucket      string
	concurrency int
	wg          sync.WaitGroup
}
type ProcessResult struct {
	FileName string
	Users    FoundUsers
	Error    error
}

// func NewS3Processor(bucket string, concurrency int, roleArn string, profile string) (*S3Processor, error) {

// 	var cfg aws.Config
// 	var err error

// 	if profile != "" {
// 		// Load config with specific profile
// 		cfg, err = config.LoadDefaultConfig(context.Background(),
// 			config.WithSharedConfigProfile(profile),
// 		)
// 	} else {
// 		// Load default config
// 		cfg, err = config.LoadDefaultConfig(context.Background())
// 	}
// 	if err != nil {
// 		return nil, fmt.Errorf("unable to load SDK config: %v", err)
// 	}
// 	if roleArn != "" {
// 		stsClient := sts.NewFromConfig(cfg)
// 		provider := stscreds.NewAssumeRoleProvider(stsClient, roleArn)

// 		cfg.Credentials = aws.NewCredentialsCache(provider)
// 	}

// 	return &S3Processor{
// 		client:      s3.NewFromConfig(cfg),
// 		bucket:      bucket,
// 		concurrency: concurrency,
// 	}, nil
// }

func NewS3Processor(bucket string, concurrency int, roleArn string, profile string) (*S3Processor, error) {
	cfg, err := config.LoadDefaultConfig(context.Background(),
		config.WithSharedConfigProfile(profile),
		config.WithRegion("us-east-1"), // Start with us-east-1 as default
	)
	if err != nil {
		return nil, fmt.Errorf("unable to load SDK config: %v", err)
	}

	// Create S3 client with just UsePathStyle option
	client := s3.NewFromConfig(cfg, func(o *s3.Options) {
		o.UsePathStyle = true
	})

	// Let's verify we can access the bucket first
	_, err = client.HeadBucket(context.Background(), &s3.HeadBucketInput{
		Bucket: aws.String(bucket),
	})
	if err != nil {
		return nil, fmt.Errorf("unable to access bucket: %v", err)
	}

	return &S3Processor{
		client:      client,
		bucket:      bucket,
		concurrency: concurrency,
	}, nil
}

func (p *S3Processor) ProcessDailyLogs(prefix string, assumedRoles bool) (FoundUsers, error) {
	ctx := context.Background()

	// List all objects for the given prefix
	input := &s3.ListObjectsV2Input{
		Bucket: &p.bucket,
		Prefix: &prefix,
	}

	objects, err := p.client.ListObjectsV2(ctx, input)
	if err != nil {
		return nil, fmt.Errorf("failed to list objects: %v", err)
	}

	// Create channels for jobs and results
	//jobs := make(chan *s3.Object, len(objects.Contents))
	jobs := make(chan types.Object, len(objects.Contents))
	results := make(chan ProcessResult, len(objects.Contents))

	// Start worker pool
	for i := 0; i < p.concurrency; i++ {
		p.wg.Add(1)
		go p.worker(ctx, jobs, results, assumedRoles)
	}

	// Send work to workers
	for _, obj := range objects.Contents {
		jobs <- obj
	}
	close(jobs)

	// Wait for all workers in separate goroutine
	go func() {
		p.wg.Wait()
		close(results)
	}()

	// Collect and merge results
	allUsers := make(FoundUsers)
	for result := range results {
		if result.Error != nil {
			fmt.Printf("Error processing %s: %v\n", result.FileName, result.Error)
			continue
		}

		// Merge users and their events
		for userName, foundUser := range result.Users {
			if existing, exists := allUsers[userName]; exists {
				existing.TotalEvents += foundUser.TotalEvents
				existing.Events = append(existing.Events, foundUser.Events...)
			} else {
				allUsers[userName] = foundUser
			}
		}
	}

	return allUsers, nil
}
func (p *S3Processor) worker(ctx context.Context, jobs <-chan types.Object, results chan<- ProcessResult, assumedRoles bool) {
	defer p.wg.Done()

	//use funciotn literal to handle the defers
	for obj := range jobs {
		fmt.Printf("Processing file: %s\n", *obj.Key)
		result := func(obj types.Object) ProcessResult {
			result := ProcessResult{
				FileName: *obj.Key, //dereference the pointer to string
			}

			//download the object
			resp, err := p.client.GetObject(ctx, &s3.GetObjectInput{
				Bucket: &p.bucket,
				Key:    obj.Key,
			})
			if err != nil {
				return ProcessResult{
					FileName: *obj.Key,
					Error:    fmt.Errorf("failed to download: %v", err),
				}
			}
			//close response body after we are done with it
			defer resp.Body.Close()

			//create gzip reader
			gzReader, err := gzip.NewReader(resp.Body)
			if err != nil {
				return ProcessResult{
					FileName: *obj.Key,
					Error:    fmt.Errorf("failed to create gzip reader: %v", err),
				}
			}
			defer gzReader.Close()

			var logs CloudTrailLog
			if err := json.NewDecoder(gzReader).Decode(&logs); err != nil {
				return ProcessResult{
					FileName: *obj.Key,
					Error:    fmt.Errorf("failed to parse JSON: %v", err),
				}
			}

			//process events based on mode
			if assumedRoles {
				result.Users = processAssumedRoleEvents(logs.Records, *obj.Key)
			} else {
				result.Users = processIAMUserEvents(logs.Records, *obj.Key)
			}
			return result
		}(obj)
		results <- result
	}
}

func processIAMUserEvents(events []Event, filename string) FoundUsers {
	users := make(FoundUsers)

	for _, event := range events {
		if event.UserIdentity.Type == "IAMUser" && event.UserIdentity.UserName != "" {
			t, err := time.Parse(time.RFC3339, event.EventTime)
			if err != nil {
				continue
			}

			matchedEvent := MatchedEvent{
				Timestamp:       t.Format("2006-01-02 15:04:05"),
				Action:          event.EventName,
				User:            event.UserIdentity.UserName,
				SourceIPAddress: event.SourceIPAddress,
				SourceFile:      filename,
			}

			userName := event.UserIdentity.UserName
			if foundUser, exists := users[userName]; exists {
				foundUser.Events = append(foundUser.Events, matchedEvent)
				foundUser.TotalEvents++
			} else {
				users[userName] = &FoundUser{
					UserName:    userName,
					TotalEvents: 1,
					Events:      []MatchedEvent{matchedEvent},
				}
			}
		}
	}
	return users
}

func processAssumedRoleEvents(events []Event, filename string) FoundUsers {
	users := make(FoundUsers)

	for _, event := range events {
		if isAdminUser(event.UserIdentity.PrincipalId) {
			t, err := time.Parse(time.RFC3339, event.EventTime)
			if err != nil {
				continue
			}

			matchedEvent := MatchedEvent{
				Timestamp:       t.Format("2006-01-02 15:04:05"),
				Action:          event.EventName,
				PrincipalId:     event.UserIdentity.PrincipalId,
				Arn:             event.UserIdentity.Arn,
				SessionIssuer:   event.UserIdentity.SessionContext.SessionIssuer,
				SourceIPAddress: event.SourceIPAddress,
				InvokedBy:       event.UserIdentity.InvokedBy,
				SourceFile:      filename,
			}

			usr := strings.Split(event.UserIdentity.PrincipalId, ":")[1]
			if foundUser, exists := users[usr]; exists {
				foundUser.Events = append(foundUser.Events, matchedEvent)
				foundUser.TotalEvents++
			} else {
				users[usr] = &FoundUser{
					UserName:    usr,
					TotalEvents: 1,
					Events:      []MatchedEvent{matchedEvent},
				}
			}
		}
	}
	return users
}
func findAllIAMUsers(filepath string) (map[string][]MatchedEvent, error) {
	data, err := os.ReadFile(filepath)
	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	var logs CloudTrailLog
	if err := json.Unmarshal(data, &logs); err != nil {
		return nil, fmt.Errorf("error parsing json: %v", err)
	}

	userEvents := make(map[string][]MatchedEvent)

	for _, event := range logs.Records {
		if event.UserIdentity.Type == "IAMUser" && event.UserIdentity.UserName != "" {
			t, err := time.Parse(time.RFC3339, event.EventTime)
			if err != nil {
				continue
			}

			formattedTime := t.Format("2006-01-02 15:04:05")

			matchedEvent := MatchedEvent{
				Timestamp:       formattedTime,
				Action:          event.EventName,
				User:            event.UserIdentity.UserName,
				SourceIPAddress: event.SourceIPAddress,
			}

			userEvents[event.UserIdentity.UserName] = append(
				userEvents[event.UserIdentity.UserName],
				matchedEvent)
		}
	}
	return userEvents, nil
}

func findIAMUser(filePath string, username string) ([]MatchedEvent, error) {
	data, err := os.ReadFile(filePath)

	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	var logs CloudTrailLog
	if err := json.Unmarshal(data, &logs); err != nil {
		return nil, fmt.Errorf("error parsing JSON: %v", err)
	}

	var matches []MatchedEvent
	username = strings.ToLower(username)

	for _, event := range logs.Records {
		if event.UserIdentity.Type == "IAMUser" &&
			strings.ToLower(event.UserIdentity.UserName) == username {

			t, err := time.Parse(time.RFC3339, event.EventTime)
			if err != nil {
				continue
			}

			formattedTime := t.Format("2006-01-02 15:04:05")

			matches = append(matches, MatchedEvent{
				Timestamp:       formattedTime,
				Action:          event.EventName,
				User:            event.UserIdentity.UserName,
				SourceIPAddress: event.SourceIPAddress,
			})
		}
	}
	return matches, nil

}

func findAssumedRoles(filePath string) (FoundUsers, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("error reading file: %v", err)
	}

	var logs CloudTrailLog

	if err := json.Unmarshal(data, &logs); err != nil {
		return nil, fmt.Errorf("error parsing Json: %v", err)
	}

	users := make(FoundUsers)

	for _, event := range logs.Records {

		if isAdminUser(event.UserIdentity.PrincipalId) {
			t, err := time.Parse(time.RFC3339, event.EventTime)
			if err != nil {
				continue
			}

			formattedTime := t.Format("2006-01-02 15:04:05")

			matchedEvent := MatchedEvent{
				Timestamp:       formattedTime,
				Action:          event.EventName,
				PrincipalId:     event.UserIdentity.PrincipalId,
				Arn:             event.UserIdentity.Arn,
				SessionIssuer:   event.UserIdentity.SessionContext.SessionIssuer,
				SourceIPAddress: event.SourceIPAddress,
				InvokedBy:       event.UserIdentity.InvokedBy,
			}

			var usr = strings.Split(event.UserIdentity.PrincipalId, (":"))[1]
			if foundUser, exists := users[usr]; exists {
				foundUser.Events = append(foundUser.Events, matchedEvent)
				foundUser.TotalEvents++
			} else {
				users[usr] = &FoundUser{
					UserName:    usr,
					TotalEvents: 1,
					Events:      []MatchedEvent{matchedEvent},
				}
			}

		}
	}
	return users, nil
}

func isAdminUser(event string) bool {
	if event == "" {
		return false
	}
	id := event
	if idx := strings.Index(id, ":"); idx >= 0 {
		return strings.HasPrefix(id[idx+1:], "adm")
	}
	return false
}

func main() {

	var (
		showDetail       bool
		listAll          bool
		showAssumedRoles bool
		s3Bucket         string
		s3Prefix         string
		concurrency      int
		roleArn          string
		awsProfile       string
	)

	// Define flags
	flag.StringVar(&s3Bucket, "s3-bucket", "", "S3 bucket containing CloudTrail logs")
	flag.StringVar(&s3Prefix, "s3-prefix", "", "S3 prefix for CloudTrail logs")
	flag.StringVar(&roleArn, "role-arn", "", "ARN of role to assume for S3 Access")
	flag.IntVar(&concurrency, "concurrency", 5, "Number of concurrent workers for S3 processing")
	flag.BoolVar(&showDetail, "detail", false, "show detailed event information")
	flag.BoolVar(&listAll, "list-all", false, "List all IAM users found in the logs")
	flag.BoolVar(&showAssumedRoles, "assumed-roles", false, "show Assumed role events")
	flag.StringVar(&awsProfile, "profile", "", "AWS profile to use ")

	// Parse flags
	flag.Parse()

	fmt.Printf("Command line args: %v\n", os.Args)
	fmt.Printf("Parsed values:\n")
	fmt.Printf("  s3-bucket: %q\n", s3Bucket)
	fmt.Printf("  s3-prefix: %q\n", s3Prefix)
	fmt.Printf("  role-arn: %q\n", roleArn)
	fmt.Printf("  detail: %v\n", showDetail)
	fmt.Printf("  assumed-roles: %v\n", showAssumedRoles)

	args := flag.Args()

	if s3Bucket != "" || s3Prefix != "" {
		if s3Bucket == "" || s3Prefix == "" {
			fmt.Println("Error: both -s3-bucket and -s3-prefix must be provided for S3 processing")
			flag.Usage()
			os.Exit(1)
		}
		processor, err := NewS3Processor(s3Bucket, concurrency, roleArn, awsProfile)
		if err != nil {
			fmt.Printf("error creatinf s3 processor: %v\n", err)
			os.Exit(1)
		}

		users, err := processor.ProcessDailyLogs(s3Prefix, showAssumedRoles)
		if err != nil {
			fmt.Printf("Error processing s3 logs : %v\n", err)
			os.Exit(1)
		}
		fmt.Printf("\nFound %d unique users:\n", len(users))
		fmt.Println(strings.Repeat("-", 80))

		for _, user := range users {
			fmt.Printf("User: %s", user.UserName)
			fmt.Printf("Total events: %d\n", user.TotalEvents)

			if showDetail {
				fmt.Println("Events:")
				for _, event := range user.Events {
					fmt.Printf("\tTime: %s\n", event.Timestamp)
					fmt.Printf("\tAction: %s\n", event.Action)
					fmt.Printf("\tSource IP: %s\n", event.SourceIPAddress)
					fmt.Printf("\tSource File: %s\n", event.SourceFile)
					fmt.Println()
				}
			}
			fmt.Println(strings.Repeat("-", 80))
		}
		return
	}
	if showAssumedRoles {
		if len(args) != 1 {
			fmt.Println("Error: please provide only the CloudTrail file path when using --assumed-roles")
			flag.Usage()
			os.Exit(1)
		}
		foundUsers, err := findAssumedRoles(args[0])
		if err != nil {
			fmt.Printf("Error: %v\n", err)
			os.Exit(1)
		}

		fmt.Printf("Found: %d unique SSO users: \n", len(foundUsers))
		fmt.Printf("%s", strings.Repeat("-", 80))

		for _, user := range foundUsers {
			fmt.Printf("USer: %s\n", user.UserName)
			fmt.Printf("Total events: %d\n", user.TotalEvents)

			if showDetail {

				fmt.Printf("Events")
				for _, event := range user.Events {
					fmt.Printf("	Time: %s\n", event.Timestamp)
					fmt.Printf("	ARN: %s\n", event.Arn)
					fmt.Printf("	Action: %s\n", event.Action)
					fmt.Printf("	Session Issuer Type: %s\n", event.SessionIssuer.Type)
					fmt.Printf("	Session Issuer Principal: %s\n", event.SessionIssuer.PrincipalId)
					fmt.Printf("	Source IP: %s\n", event.SourceIPAddress)
					fmt.Println()

				}

			}
			fmt.Println(strings.Repeat("-", 80))
		}
		return
	}

	if listAll {
		if len(args) != 1 {
			fmt.Println("Error: please provide only the CloudTrail file path when using --list-all")
			flag.Usage()
			os.Exit(1)
		}
		userEvents, err := findAllIAMUsers(args[0])
		if err != nil {
			fmt.Printf("Error: %v\n", err)
			os.Exit(1)
		}

		fmt.Printf("\nFound %d unique IAM users:\n", len(userEvents))
		fmt.Printf("%s", strings.Repeat("-", 80))

		for username, events := range userEvents {
			fmt.Printf("User: %s\n", username)
			fmt.Printf("Total events: %d\n", len(events))

			if showDetail {
				fmt.Println("Events:")
				for _, event := range events {
					fmt.Printf("	Time: %s\n", event.Timestamp)
					fmt.Printf("	Action: %s\n", event.Action)
					fmt.Printf("	Source IP: %s\n", event.SourceIPAddress)
					fmt.Println()
				}
			}
			fmt.Println(strings.Repeat("-", 80))
			return
		}

	}
	if len(args) != 2 {

		flag.Usage()
		os.Exit(1)
	}

	filePath := args[0]
	username := args[1]

	matches, err := findIAMUser(filePath, username)

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("\nFound %d occurences of IAM user '%s' \n", len(matches), username)

	if showDetail && len(matches) > 0 {
		fmt.Println("\nDetailed events:")
		fmt.Println(strings.Repeat("-", 80))

		for _, match := range matches {
			fmt.Printf("Time: %s\n", match.Timestamp)
			fmt.Printf("Action: %s\n", match.Action)
			fmt.Printf("User: %s\n", match.User)
			fmt.Printf("Source IP: %s\n", match.SourceIPAddress)
			fmt.Println(strings.Repeat("-", 80))
		}
	}

}

/*
go mod init iam-finder
go build -o iam-finder.exe
# For Windows
GOOS=windows GOARCH=amd64 go build -o iam-finder.exe

# For macOS
GOOS=darwin GOARCH=amd64 go build -o iam-finder-mac

# For Linux
GOOS=linux GOARCH=amd64 go build -o iam-finder-linux
*/
