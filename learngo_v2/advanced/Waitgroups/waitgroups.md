Wait group

a synchronization prmitive provided by sync package

- synchronizations = used to wait for a collection of gorouintes to finish , another mechanism for them to finish incluidng channels

- coordination - waitgroups make sure all tasks complete before moving on

- resource management = help wiht cleaning

sync -> sync.Waitgroup

basic operations
- Add(delta int) increaments waitgroup counter tells the umber of goroutines to wait for
- Done() decrements the number of goroutintes to wait for , to be called inside a goroutine
- Wait() blocks until the counter is set to zero

best practices
- avoid blocking calls in side goroutines
- use defer to call done 
- ensure proper use of add to waitgroup
- handle large numbers of goroutines
- use defer for unlocking

-pitfalls
mismatch beween add and done
deadlocks from above
