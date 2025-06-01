package main

import (
	"fmt"
	"time"
)

// func main() {

// 	//sayHello() // this will execute normally

// 	go sayHello() // go will take it out of the main thread ,
// 	//implication is that we wont see output to terminal because main function has nothign in it !
// 	//futhermore our goroutine then exists in memory but main thread is compelte
// 	time.Sleep(1 * time.Second)

// }

// go functions are just functions that leave the main thread and run in the backgroundd and come back
// to join th emain thread once the functions are finished/ready to return any value
// go do not stop the program flow and are non blocking like async await/ promises
// goroutines are mostly anonymous functions
func main() {

	var err error

	fmt.Println("begginging program")
	go sayHello()
	fmt.Println("After satHello function")

	//err = go doWork() -> because goroutines do not return anything this will error out
	go func() {
		err = doWork()
	}() // make it an anonmous function call if we want a go routine functioncall assigned to variable
	go printNumbers()
	go printLetters()

	// so because goroutines execute and the next line of execution happens immediately
	// the anonmoys function do work will not return an error here but it will after the time.sleep()
	// furthermore the dowork() thread needs to talk to the main thread and pass a vlaue
	// even though all the goroutines are working simultaneously
	if err != nil {
		fmt.Println("Error,", err)
	} else {
		fmt.Println("work completed successfully")
	}
	time.Sleep(2 * time.Second)

	// now that the main thread is checking err value again
	if err != nil {
		fmt.Println("Error,", err)
	} else {
		fmt.Println("work completed successfully")
	}

}

func sayHello() {
	time.Sleep(1 * time.Second)

	fmt.Println("Helo from Goroutine")
}

func printNumbers() {
	for i := 0; i < 5; i++ {
		fmt.Println("NUmber", i, time.Now())
		time.Sleep(100 * time.Millisecond)
	}
}
func printLetters() {
	for _, letter := range "abcde" {
		fmt.Println(string(letter), time.Now()) // need to convert becayse letter here is a rune which int is need to type convert since
		time.Sleep(200 * time.Millisecond)
	}
}

// hadnling errrors with go routines without using channels
func doWork() error {
	time.Sleep(1 * time.Second)

	return fmt.Errorf("An error occured in dowork")
}
