package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

type AtomicCounter struct {
	count int64
}

func (ac *AtomicCounter) increment() {

	//can do because ac.count is int64
	atomic.AddInt64(&ac.count, 1)
}

func (ac *AtomicCounter) getValue() int64 {
	return atomic.LoadInt64(&ac.count)
}

func main() {
	var wg sync.WaitGroup
	numGoroutines := 10
	counter := &AtomicCounter{}
	//value := 1

	for range numGoroutines {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for range 1000 {
				//counter.increment()
				//value++  // this will produce an unreliable result
			}
		}()
	}
	wg.Wait() // blocks main method from proceeding until all gorotuines have finished executing
	fmt.Printf("Final counter value : %d \n", counter.getValue())
	//fmt.Printf("Final counter value : %d \n", value)
}
