package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 2)
	//also block on recieve if buffer is empty , cause deadlock
	//fmt.Println("Value" , <- ch)

	go func() { // keep in mind its happening really fast go runtime scheduler
		time.Sleep(2 * time.Second) //the go runtime scheduler will pause the go routine
		ch <- 1
		ch <- 2 // execution starts at the right and ends at the left . i.e 2 is first value ch is last
		// this means in the next line of execution where println is the value is ready to be consumerd
		// by the prinln on line 21
	}()

	fmt.Println("Value consumed: ", <-ch)
}
func buffered() {

	//make (chan Type , capacity)

	// unlike unbuffered channels we do not need an immediate reciever
	ch := make(chan int, 2)
	ch <- 1
	ch <- 2
	// at this point of execution channel is full and blocking begins
	fmt.Println("Value Recieved: ", <-ch)
	fmt.Println("Value Received: ", <-ch)

	ch <- 3
	fmt.Println("Buffered channels")
}
