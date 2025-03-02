package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"strings"
	"time"
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
}

type FoundUser struct {
	UserName    string
	TotalEvents int
	Events      []MatchedEvent
}

type FoundUsers map[string]*FoundUser

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
	)

	//detailFlag := flag.Bool("detail", false, "show detailed event information")
	flag.BoolVar(&showDetail, "detail", false, "show detailed event information")
	flag.BoolVar(&listAll, "list-all", false, "List all Iam user found in the logs")
	flag.BoolVar(&showAssumedRoles, "assumed-roles", false, "show Assumed role events")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage:\n")
		fmt.Fprintf(os.Stderr, " %s [--detail] <cloudtrail-file> <username>\n", os.Args[0])
		fmt.Fprintf(os.Stderr, " %s --list-all <cloud-trail-file>\n", os.Args[0])
		fmt.Fprintf(os.Stderr, " %s --assumed-roles <cloud-trail-file>\n", os.Args[0])
		flag.PrintDefaults()
	}

	flag.Parse()

	args := flag.Args()
	if showAssumedRoles {
		if len(args) != 1 {
			fmt.Println("Error: please provide only the CloudTrail file path when using --list-all")
			flag.Usage()
			os.Exit(1)
		}
		foundUsers, err := findAssumedRoles(args[0])
		if err != nil {
			fmt.Printf("Error: %v\n", err)
			os.Exit(1)
		}

		fmt.Printf("Found: %d unique SSO users: \n", len(foundUsers))
		fmt.Printf(strings.Repeat("-", 80))

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
