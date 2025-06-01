package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int)
	go func() {
		ch <- 1
	}()

	reciever := <-ch //unbuffered channel cannot hold values a // thats
	//why reciever needs to be in go routine they both need to be available at same time
	//furthermore unbuffered channles block on recieve if there no corresponding send that is ready
	fmt.Println(reciever)

}
func channels() {

	//channels need a specifiedtype to pass through
	//variable := make(chan type)

	greeting := make(chan string) // channel can be any type or it can even be a list/array of struct since this is a type
	greetString := "Hello"

	// UNBIFFERERED CHANNELS NEED AN IMMEDIATE RECIEVER AS SOON AS THEY HAVE A VALUE THEY NEED
	// A RECIVER TO SEND TO
	go func() {
		greeting <- greetString // blocking because it is continuously trying to recieve values it is ready
		greeting <- "World"
		for _, e := range "abcde" {
			greeting <- "Alphabet: " + string(e)
		}
	}()

	receiver := <-greeting
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
