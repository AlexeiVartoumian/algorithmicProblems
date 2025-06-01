
speicfy allowable channel directions
intended for use in functions and goroutines not independently
channelsa re bi-directional

defining channel directions in function signatures
send only parametes (func produceData(ch chan <- int))
receive-only parameters (func consumeData(ch <-chan int))
bidirectional channels (func bidirectional(ch chan int))