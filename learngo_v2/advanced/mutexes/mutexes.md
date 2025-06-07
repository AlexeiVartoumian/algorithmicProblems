
Mutex short for mutual exclusion

synchronization primitive for shared resources  and cricial secitons of code
- only one can hold the mutual exclusion
- multiple processes need to access a shared resources sucha s a variable , file , or database
can prevent inconsistencies

for example if someone tries to open a file and someone else tries to open a file
the first person will have write access others will have read only. 

why use mutexes ?
- data integrity
- synchronization
- avoid race conditions

how is mutual exclusion achieved
- locks (mutexts)
- semaphores
- monitors
- critical sections

basic operations
- Lock()
- Unlock()
- TryLock()

ofetn used in structs on thier fields or the struct as a whole
-encapsualtion
- convenience
- readiability

best practise 
- minimize lock duration
- avoid nested locks
- prefer sync.RWmutext for read hevery workloads
- check ofr deadlocks
- use defer for unlcoking 

pitfalls
- deadlocks
- performance issues
- starvation 
