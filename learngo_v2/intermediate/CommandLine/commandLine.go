package main

import (
	"flag"
	"fmt"
	"os"
)

func main() {

	//go run path-> to -> file -> output = output the run
	fmt.Println("Command", os.Args[0])

	//usage go run file hello -> runs argument1 hello
	fmt.Println("Argument1:", os.Args[1])

	// iterartting on args
	for i, arg := range os.Args {
		fmt.Println("Argument", i, ":", arg)
	}

	var name string
	var age int
	var male bool

	//flag accepts pointer makes sensee we want to refer to the same thing
	flag.StringVar(&name, "name", "John", "Name of the user") // val , name of comm , default value , descriptor
	flag.IntVar(&age, "age", 18, "age of user")
	flag.BoolVar(&male, "male", true, "gender of user")

	//need to parse args
	flag.Parse()
	fmt.Println("Name", name)
	fmt.Println("Age", age)
	fmt.Println("male", male)

	// usage would be go run CommandLine.go -name James - age 50 -male true
	// note how we need a flag also enclose in quotes for say "James Doe" otherwise treated as diffrent argument

}
