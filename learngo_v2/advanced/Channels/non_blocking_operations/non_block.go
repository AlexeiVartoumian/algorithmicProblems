package main

import (
	"fmt"
	"time"
)

func main() {

	//non blocking recieve operation example using select
	//ch := make(chan int)

	// select {
	// 	case msg := <-ch:
	// 		fmt.Println("Recieved: msg" , msg )
	// 	default :
	// 	fmt.Println("No messages available")
	// }

	// // non blocking send operation example
	// select {
	// 	case ch <- 1 :
	// 		fmt.Println("Sent message")
	// 	default:
	// 		fmt.Println("Channel is not ready to recieve")
	// }

	// non blocking operation in real time systems
	data := make(chan int)
	quit := make(chan bool) //gracefully exit the program see line 53

	go func() {
		for {
			select {
			case d := <-data:
				fmt.Println("data received", d)
			case <-quit:
				fmt.Println("Stopping...")
				return // quit the channel consumptions

			default:
				fmt.Println("waiting for data...")
				time.Sleep(5000 * time.Millisecond)
			}

		}
	}()

	for i := range 5 {
		data <- i
		time.Sleep(time.Second)
	}
	quit <- true

}
