package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	// this style gives flag package a reference to a string varaible
	//var stringFlag string
	//flag.StringVar(&stringFlag, "user", "john", "name of user")

	// this approach the flag package creates the variable and reutns the reference to it .
	stringFlag := flag.String("user", "Guest", "Name of user")

	flag.Parse()

	//fmt.Println(stringFlag) // this one for line 12
	fmt.Println(*stringFlag)
	subcommand1 := flag.NewFlagSet("firstsub", flag.ExitOnError)
	subcommand2 := flag.NewFlagSet("secondsub", flag.ExitOnError)

	//saving subcommand into a varaible
	firstFlag := subcommand1.Bool("processing", false, "command  processing status")
	secondFlag := subcommand1.Int("bytes", 1024, "byte length of result")

	flagsc2 := subcommand2.String("language", "Go", "ENter your language")

	if len(os.Args) < 2 {
		fmt.Println("This programm needs args")
		os.Exit(1)
	}

	//consider that becasue the flags are accepting strings and they are pointers
	// if we wish to see the values we must dereferce tge pointer and access the value stores in mem locaiton
	switch os.Args[1] {
	//determine value of input arg
	case "firstsub":
		subcommand1.Parse(os.Args[2:]) // get all args after run
		fmt.Println("Subcommand1")
		fmt.Println("processing:", *firstFlag)
		fmt.Println("bytes", *secondFlag)

	case "secondSub":
		subcommand2.Parse(os.Args[2:])
		fmt.Println("Subcommand2:")
		fmt.Println("language", *flagsc2)
	default:
		fmt.Println("no subcommand entered")
		os.Exit(1)
	}

	// go run subcommand.go firstsub -processing=true -bytes=256
}
