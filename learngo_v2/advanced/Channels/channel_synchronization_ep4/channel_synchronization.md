
channel synchrnoization co-ordination of goroutines to ensure orderly execution and data exchange

mechanism to block and unblock channels based on state

- ensures data is properly exchanged between goroutines
- coordinates execution flow to avoid race conditinos and ensure predicatable behaviour
- manages lifecycles of goroutines

applications i.e news feed needs to be updated different views needed for derrent users , financial trades
// observe main2 func using fan in fan out pattern
common pitfalls
- avoid deadlocks
- close channels
- avoid unnecessary blocking

