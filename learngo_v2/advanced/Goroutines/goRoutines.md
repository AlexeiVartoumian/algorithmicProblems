Goroutines

why use goroutines -> lightwieght threads manged by go routines

-efficeintly handle parrallel tasks such as I/o operations , calculations and more

-provide a way to perform tasjs concurently without manually managing threads

basics of goroutines
-creating goroutine
-go routine lifecycle
-goroutine scheduling

gorotunine scheduling in go
managed by go runtome scheduiler , uses m:n scheduling model = m go routines are mapped onto n os.threads , 

m:n scehduling model -> i.e your processor  has 4 core 8 thread computer and goroutines are mapped onto them

goroutines are non-blocking since they run concurrently with the main goroutine , managed by the go runtime

efficient multiplexing -> switching between threads


common pitfalls + best prac
-avoiding goroutine leaks i.e main thread finished before goroutine executing or infinite loop in goroutine 
, limiting goroutine creation 
, proper error handiling 
, sychronization


When to Use Goroutines
1. I/O Operations (Network, Files, Database)
go// Instead of waiting for each API call sequentially
go fetchUserData(userID)
go fetchUserPosts(userID)  
go fetchUserSettings(userID)
2. Independent Tasks Running in Parallel
go// Processing multiple files simultaneously
for _, filename := range files {
    go processFile(filename)
}
3. Background Tasks
go// Periodic cleanup, monitoring, logging
go func() {
    ticker := time.NewTicker(5 * time.Minute)
    for range ticker.C {
        cleanupTempFiles()
    }
}()
4. Producer-Consumer Patterns
go// One goroutine generates work, others consume it
go producer(workChannel)
go consumer(workChannel)
go consumer(workChannel)
5. Web Servers (Each Request Gets Its Own Goroutine)