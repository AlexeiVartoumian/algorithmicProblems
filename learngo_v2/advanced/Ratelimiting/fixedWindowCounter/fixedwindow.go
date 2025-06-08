package main

import (
	"fmt"
	"sync"
	"time"
)

// becasue mutex is used can use go func
type RateLimiter struct {
	mu        sync.Mutex
	count     int
	limit     int
	window    time.Duration
	resetTime time.Time
}

func NewRateLimiter(limit int, window time.Duration) *RateLimiter {
	return &RateLimiter{
		limit:  limit,
		window: window,
	}
}

func (rl *RateLimiter) Allow() bool {
	rl.mu.Lock()
	defer rl.mu.Unlock() //enter ciritcal section

	now := time.Now()
	if now.After(rl.resetTime) {
		rl.resetTime = now.Add(rl.window)
		rl.count = 0
	}
	if rl.count < rl.limit {
		rl.count++
		return true
	}
	return false
}

func main() {
	rateLimiter := NewRateLimiter(5, 2*time.Second)

	var wg sync.WaitGroup
	for range 10 {
		wg.Add(1)
		//can do because mutex are being used
		go func() {
			if rateLimiter.Allow() {
				fmt.Println("Request allowed")
			} else {
				fmt.Println("request denied")
			}
			wg.Done()
		}()
		//can use waitgroups wait for goroutines instead of time.Sleep
		//time.Sleep(200 * time.Millisecond)
	}
	wg.Wait()
}
