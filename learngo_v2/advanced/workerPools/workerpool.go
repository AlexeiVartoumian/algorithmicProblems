package main

import (
	"fmt"
	"time"
)

//BASIC WORKER POOL PATTERN

// represets a worker that reciees jobs from tasks channel processes them and send them to send only channel results
func worker(id int, tasks <-chan int, results chan<- int) {

	//continously recieves tasks from task channel until it is closed
	for task := range tasks {
		fmt.Printf("Worker %d rpocessing task %d\n", id, task)
		//simulate work
		time.Sleep(time.Second)
		results <- task * 2
	}
}

func exmple() {
	numWorkers := 3
	numJobs := 10
	//both channels below are bufffered channels
	tasks := make(chan int, numJobs)
	results := make(chan int, numJobs)

	//creaate workers
	for i := range numWorkers {
		// each gorotine worker is passed its id denoted by i and the results channel to send to
		// go func recieves the task channel and the results channel
		// and a lightwieght thread is spawned
		go worker(i, tasks, results)
	}

	//send values to the tasks channel where the goroutines are waiting for tasks currently an empty channel
	for i := range numJobs {
		tasks <- i
	}

	close(tasks)

	//collect the results
	for range numJobs {
		result := <-results
		fmt.Println("Result: ", result)
	}
	//this all works because of the buffereed storage

}
