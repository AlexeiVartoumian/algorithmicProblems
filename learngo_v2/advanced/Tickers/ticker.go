package main

import (
	"fmt"
	"time"
)

func main() {
	ticker := time.NewTicker(time.Second)
	stop := time.After(5 * time.Second)

	defer ticker.Stop()

	for {
		select {
		case tick := <-ticker.C:
			fmt.Println("tick at ", tick)
		case <-stop:
			fmt.Println("stopping ticker")
			return
		}
	}
}

func periodicTask() {
	fmt.Println("Performing periodic task at: ", time.Now())
}

func basicExample() {
	ticker := time.NewTicker(time.Second)
	defer ticker.Stop()
	// this will continue running this periodic task will continue to run i.e polling or log schdeuld , periodic tasks
	for {
		select {
		case <-ticker.C:
			periodicTask()
		}
	}
}

func tickerdemo() {

	//given a duration of time .second
	ticker := time.NewTicker(2 * time.Second)

	// we always have to stop a ticker otherwise leaky resourcews
	defer ticker.Stop()
	i := 1

	for range 5 {
		i *= 2
		fmt.Println(i)
	}

	//for tick := range ticker.C {
	//fmt.Println("tick at ", tick)
	//}
	// for range ticker.C {
	// 	i *= 2
	// 	fmt.Println(i)
	// }

}
