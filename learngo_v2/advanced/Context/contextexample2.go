package main

import (
	"context"
	"fmt"
	"time"
)

func checkEvenOdd(ctx context.Context, num int) string {

	//can use context to carry cancellation signals
	select {
	//can use the context method done to recieve data from the channel
	case <-ctx.Done(): // this will check to see if the channel has been closed or not which in prog below is true since
		//of timeout. useful to abort indefinite operations for example large data transfer from a api.
		return "Operation canceled"
	default:
		if num%2 == 0 {
			return fmt.Sprintf("%d is even", num)
		} else {
			return fmt.Sprintf("%d is odd", num)
		}
	}
}

func main() {
	ctx := context.TODO()
	result := checkEvenOdd(ctx, 5)
	fmt.Println("Result with context.TODO():", result)

	ctx = context.Background()
	//WithTimeoutmethod available on context needs a parent context
	ctx, cancel := context.WithTimeout(ctx, 1*time.Second) // here we create a context with a deadline of 1 second
	defer cancel()

	fmt.Println("result from timeout context", result)
	time.Sleep(3 * time.Second)
	result = checkEvenOdd(ctx, 15)
	fmt.Println("result after timeout", result)
}
