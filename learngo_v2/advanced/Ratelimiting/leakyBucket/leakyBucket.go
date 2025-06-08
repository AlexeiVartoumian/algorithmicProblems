package main

import (
	"fmt"
	"sync"
	"time"
)

type LeakyBucket struct {
	capacity int
	leakRate time.Duration
	tokens   int
	lastLeak time.Time
	mu       sync.Mutex
}

func NewLeakyBucket(capacity int, leakRate time.Duration) *LeakyBucket {
	return &LeakyBucket{
		capacity: capacity,
		leakRate: leakRate,
		tokens:   capacity,
		lastLeak: time.Now(),
	}
	// start with a full bucket and timestamp of creationf
}

func (lb *LeakyBucket) Allow() bool {
	lb.mu.Lock() // only one go routine can access at a time
	defer lb.mu.Unlock()

	//add more tokens based on the leakrate passed in initialisation of bucket
	now := time.Now()
	elapsedTime := now.Sub(lb.lastLeak)           // how much time has passed since last refill
	tokensToAdd := int(elapsedTime / lb.leakRate) // 0.2 /0.5 result is 0.4 tokens to add is 0 ,
	//if leakrate is grearter then elapsedtime then no tokens are added
	lb.tokens += tokensToAdd

	if lb.tokens > lb.capacity {
		lb.tokens = lb.capacity
	}
	//elapsed time is not a definitive measure of a token being added , leakrate is the determinant
	lb.lastLeak = lb.lastLeak.Add(time.Duration(tokensToAdd) * lb.leakRate)

	fmt.Printf("tokens added %d Tokens subtracted %d , Total tokens %d\n", tokensToAdd, 1, lb.tokens)
	fmt.Printf("Last leak time: %v", lb.lastLeak)
	if lb.tokens > 0 {
		lb.tokens--
		return true
	}
	return false
}

func main() {

	// tokens and leakrate
	leakyBucketInstance := NewLeakyBucket(5, 500*time.Millisecond)

	var wg sync.WaitGroup

	for range 10 {
		wg.Add(1)
		go func() {
			defer wg.Done()
			if leakyBucketInstance.Allow() {
				fmt.Println("current time", time.Now())
				fmt.Println("Request allowed")
			} else {
				fmt.Println("current time", time.Now())
				fmt.Println("Request denied")
			}
			time.Sleep(200 * time.Millisecond)
		}() //by itself bucket will rapidly run out bc goroutines!
	}
	time.Sleep(500 * time.Millisecond)
	// experiment to see after bucket is depleted how the rate limiter will work
	//only one request comes through
	for range 10 {
		wg.Add(1)
		go func() {
			defer wg.Done()
			if leakyBucketInstance.Allow() {
				fmt.Println("current time", time.Now())
				fmt.Println("Request allowed")
			} else {
				fmt.Println("current time", time.Now())
				fmt.Println("Request denied")
			}
			time.Sleep(200 * time.Millisecond)
		}() //by itself bucket will rapidly run out bc goroutines!
	}
	wg.Wait()
}
