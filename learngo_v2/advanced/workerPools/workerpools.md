workpool
design pattern to mange a fixed group of goroutines aka workers which process a queue of taks 


why use worker pools
- reosurce management / stop overwhelming system resources
- task distributions  / scale processing of tasks without creating excesssive number of gorotues
- scalability


conceptual model  / building block
- tasks 
- workers = go routines
- task queue = channel or data strucutre ot hold the go rotuenes


implementaiton steps
- create a task channel
- create worker goroutines
- distribute tasks
- graceful shutdown

best practises
- limit number of owrkers 
- properly start stop workers to ensure no resource leaks use time outs
- monitor and log worker pool


