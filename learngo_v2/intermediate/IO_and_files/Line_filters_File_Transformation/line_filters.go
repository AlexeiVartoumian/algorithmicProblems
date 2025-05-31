package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {

	file, err := os.Open("example.txt")
	if err != nil {
		fmt.Println("error opening file", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	lineNumber := 1
	keyword := "important"

	//read and filter lines
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, keyword) {
			updatesLine := strings.ReplaceAll(line, keyword, "necessary")
			fmt.Printf("Filtered line %d %v\n ", lineNumber, line)
			fmt.Printf("Updated lines%d %v\n", lineNumber, updatesLine)

			lineNumber++
		}
	}
	err = scanner.Err()
	if err != nil {
		fmt.Println("Error printing", err)
	}
}
