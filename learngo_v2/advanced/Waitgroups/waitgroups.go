package main

import (
	"fmt"
	"sync"
	"time"
)

// COnstruction Example
type Worker struct {
	ID   int
	Task string
}

// here we create a pointer reciever so to access and modify the given worker struct
func (w *Worker) PerformTask(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Printf("WorkerID %d started %s \n", w.ID, w.Task)
	time.Sleep(time.Second)
	fmt.Printf("WorkerID %d finished %s \n", w.ID, w.Task)
}

func main() {
	var wg sync.WaitGroup

	//define tasks to be performed by workers
	tasks := []string{"digging", "laying bricks", "painting"}

	for i, task := range tasks {
		worker := Worker{ID: i + 1, Task: task}
		//as we create a go routine it is ok to increment the waitgroup but do not increment inside the goroutine
		wg.Add(1)
		go worker.PerformTask(&wg)
	}
	//wait for all workers to finish
	wg.Wait()
	//construction is finished
	fmt.Println("construction finished")
}

// example with channels
func channelworker(id int, tasks <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Printf("WorkerID %d starting. \n", id)
	time.Sleep(time.Second) //simulate work
	for task := range tasks {
		results <- task * 2
	}
	fmt.Printf("WorkerId %d finished\n ", id)
}

func channelExmample() {
	var wg sync.WaitGroup
	numWorkers := 3
	numJobs := 5
	results := make(chan int, numJobs)
	tasks := make(chan int, numJobs)

	wg.Add(numWorkers)

	for i := range numWorkers {
		//set up the worker and off the main thread
		go channelworker(i+1, tasks, results, &wg)
	}

	for i := range numJobs {
		tasks <- i + 1
	}
	close(tasks) // if no close then deadlock!
	//because results is channel we need to close it once its done
	go func() {
		wg.Wait()
		//here our execution will not be blocked we want recieve the values in real time
		// therfore extract the wait i
		close(results)
		//this will close the channel once all the goroutines have finsihed. a coordination technique.
	}()

	for result := range results {
		fmt.Println("Result", result)
	}
}

// the pattern is that done will decrement the counter and is deferred until the job is done in this case
func workerbasic(id int, wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Printf("Worker %d starting \n", id)
	time.Sleep(time.Second)
	fmt.Printf("Worker %d finished\n", id)
}

func basic() {
	var wg sync.WaitGroup
	numWorkers := 3

	wg.Add(numWorkers)
	//launch workers
	for i := range numWorkers {
		go workerbasic(i, &wg)
	}
	wg.Wait() // will block until a singal is sent to wg.Done()
	fmt.Println("All workers finished")
}
