multiplexing is process of handling multiple channel operationa simultaneious

allows to wait on multiple operations and react to teh first ready one

like switch statement

why use?
 - manages multiple concurrent operations within a single goroutine
 - efficiently handle operations without blcing
 - cna implement timeouts and cancellations on channels using multiplexing

 basic language constructs just like switch select case and default