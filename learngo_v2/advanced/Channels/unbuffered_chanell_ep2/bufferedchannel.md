
a buffered channel is a channel with storage

allows channels to hold a limited number of values before blocking the sender

when to use
- most important difference between unbuffered channel and buffered channels

buffered channels allow asyncrhonous communication 
i.e allow senders to continue working without blocking until buffer is full

buffered channels help in load balancing  -> handlebursts of data without immedaite synchronziation
allow better flow control can control rate of transfer between producres and consumers 
