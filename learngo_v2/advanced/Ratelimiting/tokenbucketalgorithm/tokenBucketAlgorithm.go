package main

import (
	"fmt"
	"time"
)

type RateLimiter struct {
	tokens     chan struct{}
	refillTime time.Duration
}

// func creates a new ratelimiter
func NewRateLimiter(rateLimit int, refillTime time.Duration) *RateLimiter {
	rl := &RateLimiter{
		//why use chan struct ? using empty structs in go is a mechanism in go
		// is that it has zero bytes of memory, its a token where the prescence matters not the data
		tokens:     make(chan struct{}, rateLimit), // channel will have a buffer of ratelimit
		refillTime: refillTime,
	}
	//as we send tokens to the tokens channel
	for range rateLimit {
		rl.tokens <- struct{}{} //symbolic empty tokens
	}
	// gorotuine keeps running in the background
	go rl.startRefill()
	return rl
}

func (rl *RateLimiter) startRefill() {
	//create token after a set amount of time
	ticker := time.NewTicker(rl.refillTime)
	defer ticker.Stop()
	for { // loop indefinitely
		select {
		//consume data from the channel
		case <-ticker.C:
			select {
			case rl.tokens <- struct{}{}:
			default:
			}
			//case <- ctx.Done(): would be cool to pass in context.DOne to exit the loop
			// return
		}
	}
}
func (r1 *RateLimiter) allow() bool {
	select {
	//consume data from the channel
	case <-r1.tokens:
		return true
	default:
		return false
	}
}

func main() {

	rateLimiter := NewRateLimiter(5, time.Second)

	for range 10 {
		if rateLimiter.allow() {
			fmt.Println("Request allowed")
		} else {
			fmt.Println("Reuqst denied")
		}
		time.Sleep(200 * time.Millisecond)
	}
}
