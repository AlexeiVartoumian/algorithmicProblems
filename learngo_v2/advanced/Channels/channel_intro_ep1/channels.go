package main

import (
	"fmt"
	"time"
)

func main() {

	//channels need a specifiedtype to pass through
	//variable := make(chan type)

	greeting := make(chan string) // channel can be any type or it can even be a list/array of struct since this is a type
	greetString := "Hello"

	//recieve data into channel
	//keep in mind because the go func here is anonumous it can access variables from the outerscope
	go func() {
		greeting <- greetString // blocking because it is continuously trying to recieve values it is ready
		//to recieve continues flow of data
		//keep in mind that greeting channel is constantly open ,
		// i.e imagine weather api when we get data periodically we can now have open stream of data
		greeting <- "World"
		greeting <- "thirval"
		for _, e := range "abcde" {
			greeting <- "Alphabet: " + string(e)
		}
	}()

	receiver := <-greeting // reciever variable is recieving from greeting channel
	// note that receiver is also part of the main go rotuine and that therefore communication
	// between two go-roytines ahs been acheived

	fmt.Println("First receiver channel  value", receiver)
	// note the second value will need to be reassigned to get it
	receiver = <-greeting
	fmt.Println("Second reciever", receiver)

	go func() {
		receiver = <-greeting
		fmt.Println("third value passed to reciever channel ", receiver) // this could be sending values somewhere else i.e frontend
	}()

	// reading multiple values from channel
	for range 5 {
		rcvr := <-greeting
		fmt.Println(rcvr)
	}

	//keep in mind that this go routine need time to execute to avoid memory leak on the main go thread executing!
	time.Sleep(1 * time.Second)
	fmt.Println("End of program")
}
