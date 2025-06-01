CHannels 

why use channles
- enable safe and efficent commincation between concurrent goroutines
- help synchronize and manage the flow of data in concurrent programs 

what are channels 
they are a pipe where if data flows in this pipe there absolutely must be 
an avaialble sender and reciever present at the same time
// channels will not work inside the main function or any function they will onlu work with goroutine

goroutines are non-blocking since they run concurrently with the main goroutine , managed by the go runtime

the main threaswhereas channels are BLOCKING

unbuffered channels need a goroutine since as soon as it gets a value it will send it
therefore we always send values inside the goroutine where reciver can be on the main thread
order of operations matter

furthermore unbuffered channles block on recieve if there no corresponding send that is ready

channles require closing and buffering as well

basics of channels 
- creating channels (makle(channel))