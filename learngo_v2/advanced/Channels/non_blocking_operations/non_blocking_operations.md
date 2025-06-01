
a non-blokcing operatoions on channels allow a go routine to perform a channel operation

like send or recieve without getting stuck if the channel is not ready

why use ?
- avoid deadlocks
- prevent goroutines from waiting indefinitely
- enhance concurrency

best prac for non-blocking operaitons