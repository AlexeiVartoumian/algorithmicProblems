package main

import (
	"fmt"
	"time"
)

type StatefulWorker struct {
	count int
	ch    chan int
}

func (w *StatefulWorker) Start() {
	go func() {
		//infiinte loop to be limited in main funciton
		for {
			select {
			//receive the value from channel and update the struct reference
			case value := <-w.ch:
				w.count += value
				fmt.Println("Current count:", w.count)
			}
		}
	}()
}
func (w *StatefulWorker) Send(value int) {
	w.ch <- value
}

func main() {

	statefulWorker := &StatefulWorker{
		ch: make(chan int),
	}
	statefulWorker.Start()

	for i := range 5 {
		statefulWorker.Send(i)
		time.Sleep(500 * time.Millisecond)
	}

}
