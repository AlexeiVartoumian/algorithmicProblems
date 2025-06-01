package main

import (
	"fmt"
	"time"
)

// synchornizing data exchange
func main() {
	data := make(chan string)

	go func() {
		for i := range 5 {
			data <- "hello " + string('0'+i)
			time.Sleep(100 * time.Millisecond)
		}
		close(data) // have to close the channel otherwise the loop below will keep iterating
		// over the data channel crashing program.
		//this will signal to reciever there is no sending happening
	}()

	// if close(data) was here main thread will shut chanell down meaning no data to reciver

	// iterating over a channel where this is an alternate way to create a reciever
	// not creating a reciver with arrow operator
	for value := range data {
		fmt.Println("recevied value ", value, ":", time.Now())
	}
}

// synchonizaing signal exchange but the order of execution of go routines is random
// main two is using fan in fan out pattern
func main2() {

	numGoroutines := 3
	done := make(chan int, 3)

	//synchronizing channels
	for i := range numGoroutines {

		go func(id int) {
			fmt.Printf("Goroutine %d working... \n", id)
			time.Sleep(time.Second)
			done <- i
		}(i)
	}

	for range numGoroutines {
		//<-done //wait for each gorouitne to finish , by itsels will throw error becaue
		// need two commuincation gorotuines
		fmt.Println("executing reciver loop", <-done)
	}
	fmt.Println("all go rotuine sot finish")

}

// func main() {

// 	// consider a chan transporting information that can be serialized
// 	done := make(chan struct{})

// 	go func() {
// 		fmt.Println("Working...")
// 		time.Sleep(2 * time.Second) // this represents a task i.e heavy calculation
// 		done <- struct{}{}          // send a blank value
// 	}()

// 	<-done
// 	fmt.Println("Finished")

// }
