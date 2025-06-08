statefulGoroutine 

a stateful goroutines updates or maintains its own internal state across multiple interactions
it allows go routines to manage themselves

when tasks need to 

why use staeful goroutines
- state management
- concurrency
- task execution

generally use mutexes and locks or atomic operaitons
use channels for communication

common use cases
- task processing 
- stateful services
- data stream processing 

key conecpt of stateful goroutines
- state preservation
- concurrency management
- lifecycle management

best practises
- encapsulate stste , synchrnoize access . monitor devys