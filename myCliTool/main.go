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
	Type     string `json:"type"`
	UserName string `json:"userName,omitempty"`
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
	SourceIPAddress string
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

func main() {

	var (
		showDetail bool
		listAll    bool
	)

	//detailFlag := flag.Bool("detail", false, "show detailed event information")
	flag.BoolVar(&showDetail, "detail", false, "show detailed event information")
	flag.BoolVar(&listAll, "list-all", false, "List all Iam user found in the logs")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage:\n")
		fmt.Fprintf(os.Stderr, " %s [--detail] <cloudtrail-file> <username>\n", os.Args[0])
		fmt.Fprintf(os.Stderr, " %s --list-all <cloud-trail-file>\n", os.Args[0])
		flag.PrintDefaults()
	}

	flag.Parse()

	args := flag.Args()

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
