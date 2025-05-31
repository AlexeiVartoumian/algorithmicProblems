package main

// embed directive takes a special commment to know that a file needs to be embededed. belw is the comment
//and the steps needed for this

import (
	"embed"
	"fmt"

	//_ "embed" // here we are using the embed for its side effects i.r the directive but not any functions
	//so we are using a blank import here which is done underscore
	// in other words if only using side effect for files only see line 16
	"io/fs"
	"log"
)

//go:embed example.txt
var content string

//go:embed basics
var basicsFolder embed.FS

func main() {

	fmt.Println("Embedded content", content)

	embededed_file, err := basicsFolder.ReadFile("basics/somefile.txt")
	if err != nil {
		fmt.Println("error happended", err)
	}
	fmt.Println("Embedded file content", string(embededed_file))

	// now that we embed a folder it makes sense to walk trough the folder
	//basicsFOlder is embed.fs  where package fs implements interface
	err = fs.WalkDir(basicsFolder, "basics", func(path string, d fs.DirEntry, err error) error {

		if err != nil {
			fmt.Println(err)
			return err
		}
		return nil
	})

	if err != nil {
		log.Fatal(err)
	}

}
