package main

import (
	"fmt"
	"time"
)

func main() {

	ch1 := make(chan int)
	ch2 := make(chan int)

	//below will select first available channel and unlike commented code,
	//can now handle non-senifng channel with default
	go func() {
		time.Sleep(time.Second)
		ch1 <- 1
	}()
	go func() {
		time.Sleep(time.Second)
		ch2 <- 2
	}()

	time.Sleep(2 * time.Second)
	//enclosing into loop since we for demo we want all values from respective channel
	for range 2 {
		// will prvoide the first avaialble channel
		select {
		case msg1 := <-ch1:
			fmt.Println("Received from ch1", msg1)

		case msg2 := <-ch2:
			fmt.Println("Recived from ch2", msg2)
		default:
			fmt.Println("No channel ready ")
		}
	}

	ch := make(chan int)

	go func() {
		time.Sleep(2 * time.Second)
		ch <- 1
		close(ch) // if continous flow of data can defer
	}()
	//iterating on constant stream of meesages
	for {
		select {
		case msg, ok := <-ch: // channels also carry another boolean value to state if they are open or closed
			if !ok {
				fmt.Println("Channel CLosed")
				//say open channel used for  chat app a user logs out an
				//need to close	 the channel
				return //can return out of the function
			}
			fmt.Println("Receievd", msg)
		case <-time.After(3 * time.Second):
			fmt.Println("Timeout")
		}
	}

}
