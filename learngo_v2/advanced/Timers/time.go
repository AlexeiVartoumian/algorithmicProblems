package main

import (
	"fmt"
	"time"
)

func main() {
	timer1 := time.NewTimer(1 * time.Second)
	timer2 := time.NewTimer(2 * time.Second)

	select {
	case <-timer1.C:
		fmt.Println("|Timer1 expired")
	case <-timer2.C:
		fmt.Println("timer2 expired")
	}
}

// ================ SCHEDULING DELAYED OPERATIONS
func main2() {
	timer := time.NewTimer(2 * time.Second)

	go func() {
		<-timer.C
		fmt.Println("Delayed operation executed")
	}()
	fmt.Println("Waiting")
	time.Sleep(3 * time.Second) ////need blocking operation on the mai thread to see the delayed op
	fmt.Println("End of program")
}

// ============ HANDLING TIMEOUT ================
func longRunningOperation() {
	for i := range 20 {
		fmt.Println(i)
		time.Sleep(time.Second)
	}
}

func timeouts() {
	timeout := time.After(2 * time.Second)
	done := make(chan bool)

	go func() {
		longRunningOperation()
		done <- true // signal that work is done
	}()
	select {
	case <-timeout:
		fmt.Println("Operation times out ")
	case <-done:
		fmt.Println("operation completed")
	}
}

//=====================EXAMPLE==============================

func example() {

	fmt.Println("")
	// timer is a struct . it aslso has a field C which gives us channel
	timer := time.NewTimer(2 * time.Second)

	stopped := timer.Stop()
	if stopped {
		fmt.Println("Timer.Stopped")
	}
	timer.Reset(time.Second)
	fmt.Println("Timer rest")
	<-timer.C //blocking in nature because channel and can use in gorotuine to be non-blocking
	fmt.Println("timer expired")

}
