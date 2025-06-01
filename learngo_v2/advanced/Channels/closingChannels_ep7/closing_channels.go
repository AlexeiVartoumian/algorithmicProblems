package main

import "fmt"

func producer(ch chan<- int) {
	for i := range 5 {
		ch <- i
	}
	close(ch)
}

func filter(in <-chan int, out chan<- int) {
	for val := range in {
		if val%2 == 0 {
			out <- val
		}
	}
	close(out) // channel 2 receving is closed once work is done
}
func main() {

	ch1 := make(chan int)
	ch2 := make(chan int)

	go producer(ch1)
	go filter(ch1, ch2)

	for val := range ch2 {
		fmt.Println(val)
	}
	//ranging over a closed channel
	// ch := make(chan int)
	// go func() {
	// 	for i := range 5 {
	// 		ch <- i
	// 	}
	// 	close(ch)
	// }()

	// for val := range ch {
	// 	fmt.Println("recieved ", val)
	// }
	//recieving from a closed channel
	// ch:= make(chain int)
	// close(ch)

	// val , ok := <- ch // recall that channels carry boolean value to signal they are closed
	// if !ok {
	// 	fmt.Println("Channel is closed")
	// 	//return
	// }
	// fmt.Println(val)

	//simple closing channel example
	// ch := make(chan int)

	// go func() {
	// 	for i := range 5 {
	// 		ch <- i
	// 	}
	// 	close(ch)
	// }()

	// for val := range ch {
	// 	fmt.Println(val)
	// }
}
