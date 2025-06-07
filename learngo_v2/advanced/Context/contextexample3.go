package main

import (
	"context"
	"fmt"
	"log"
	"time"
)

func doWork(ctx context.Context) {

	for {
		select {
		case <-ctx.Done():
			fmt.Println("Work cancelled", ctx.Err()) // context also has error tyoe
			return

		default:
			{
				fmt.Println("Working")
			}
			time.Sleep(500 * time.Millisecond)
		}
	}
}

func main() {
	rootctx := context.Background() // not someting working in the background its a variable
	//rather its always ready to be used in the background a baseline for other contexts

	// rootctx, cancel := context.WithTimeout(rootctx, 2*time.Second) // returns two vals time will be calculated at this point
	// //at which point a cancellation signal will be sent

	rootctx, cancel := context.WithCancel(rootctx) // can do the above but manually

	go func() {
		time.Sleep(2 * time.Second) // simulating a heavy time consuming opertaion only after task is done is
		cancel()                    // this task finsihed
	}()
	defer cancel()

	rootctx = context.WithValue(rootctx, "requestID", "8347462dns-okq")
	rootctx = context.WithValue(rootctx, "ip", "10.123.421.55")
	rootctx = context.WithValue(rootctx, "OS", "operatingSystem")

	go doWork(rootctx)
	time.Sleep(3 * time.Second)

	requestId := rootctx.Value("requestID")

	if requestId != nil {
		fmt.Println("RequestUd", requestId)
	} else {
		fmt.Println("No request id doing")
	}
	logWithContext(rootctx, "this is a test log message")
}

func logWithContext(ctx context.Context, message string) {
	requestIDVal := ctx.Value("requestID")
	log.Printf("RequestID: %v - %v", requestIDVal, message)
}
