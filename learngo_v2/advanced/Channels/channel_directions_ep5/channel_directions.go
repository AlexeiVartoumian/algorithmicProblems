package main

import "fmt"

func main() {

	//declare bi-directional channel
	ch := make(chan int)

	// //define in function signature direction of chnnale
	// go func(ch chan<- int) {

	// 	for i := range 5 {
	// 		ch <- i // remember executing from right to left
	// 	}
	// 	close(ch) // nned to close a channel to avoid memory leaks
	// }(ch)

	//here we can consume from the chanel
	// for value := range ch {
	// 	fmt.Println("Received: ", value)
	// }
	producer(ch)
	consumer(ch)

}
func producer(ch chan<- int) {
	go func() {
		for i := range 5 {
			ch <- i
		}
		close(ch)
	}()
}

//here we can consume from the chanel
func consumer(ch <-chan int) {
	for value := range ch {
		fmt.Println("Recieved: ", value)
	}
}
