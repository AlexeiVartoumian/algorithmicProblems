
buffred channels allow channels allow them to hold some amount of storage before blocking sender
- if unbuffered channels are a pipe then buffered channels is like a tap

good for managing concurrency
-async communication
-load balancing
- flow control
why use ?
unlike unbuffered channels that need immediate receiver not so with bufferd channel since can hold value

createing buffered channels
- make (chan Type ,capacity)
- buffer capacity

key concepts of channel buffering
blocking behaviour , non blocking operations, impact on performance

best prac for using buffered channels
- avoid over buffering
- graceful shutdown
- monitoring buffer usage