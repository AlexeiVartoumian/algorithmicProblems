
Atomic counter
used to manage and track primitive type counts without having the need for locking
atomic here means indivisible and uninterrupatble , 
once the operation starts it runs to completoin , no other thread can observe or intefere with the state.
implemented with low level instructions.

threadsafe oeprations on shared variables without using locks

why use Atomic counter
- performance , faster then mutex
- simplicity starightforward way to mange counters
- conccurency  like mutexes ensure counter updates are safe
- lost updates and inconsistent reads i.e data race


atomic operations in Go
- window duration
- request counting
- reset mechanism

sync/atomic package
- atomic.AddInt32/atomic.Addint64
- atomic.LoadInt32/atomic.Loadint64
- atomic.StoreInt32/atomic.Storeint64
- atomic.StoreInt32/atomic.Storeint64