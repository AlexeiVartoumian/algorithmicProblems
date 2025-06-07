package main

import (
	"fmt"
	"sync"
)

func main() {
	var counter int
	var wg sync.WaitGroup
	var mu sync.Mutex

	numGoroutines := 5
	wg.Add(numGoroutines)

	increment := func() {
		defer wg.Done()
		for range 1000 {
			mu.Lock()
			counter++
			mu.Unlock()
		}
	}
	for range numGoroutines {
		go increment()
	}
	wg.Wait()
	fmt.Printf("final counter value %d \n", counter)
}

// consider the case where mutliple goroutines want to update THE SAME VALUE
// they will perform an operation on this value and save whatever value they recieved unto the variable.
// this is a critical section! need a lock in this case
// the counter example is a contrived example but it should highlight
// allowoing for parallel work to happen except in the case syncronization is needed for a shared resource

type counter struct {
	mu    sync.Mutex // iniatited with sync package
	count int        // multiple goroutines will try to modify
}

// use method reciever to point to the counter struct to get the lock mechanism avaialable on the sync.mutex
func (c *counter) increment() {
	// no one can mutate the value until funciton exits
	c.mu.Lock()
	//before a function returns
	defer c.mu.Unlock()
	c.count++
}

func (c *counter) getValue() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.count
}

func mutexexample() {

	var wg sync.WaitGroup
	counter := &counter{} // creates a new instance of counter struct and returns a pointer to it

	//numGoroutines := 10

	//wg.Add(numGoroutines)
	//starting 10 go routines will perform increment 1000 times
	for range 10 {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for range 1000 {
				counter.increment()

			}
		}()
	}

	//wait group ensures all workers will complete before the getting the value
	wg.Wait()
	fmt.Printf("Final counter value: %d\n", counter.getValue())
}
