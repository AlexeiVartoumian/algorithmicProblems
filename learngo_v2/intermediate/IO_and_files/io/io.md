
faciliates interactions with various data sources (files , networks , in-memoery buffers)
provides a consistent interface for handling i/o operations 

CORE INTERFACES
io.Reader -> read data from a source and the method is read , implemented in strings.reader and implemented by bytes.buffer
io.Writer -> writing data to a destination strings.builder use this os.File struct implements this , bytes.buffer and strings.Builder

io.closer

common types and functions

io.Reader -> implemented by os.file also impelmented by strings.Reader also implemneted by bytes.buffer also io.writer

io.Writer -> implemented by os.file struct bytes.buffer and strings.builder

io.Copy -> copies from io.reader to io .writer

io.multiReader() -. variadic arguments

io.Pipe() -> simple way to pass data from different parts of a prgroam used in many situations between dfiferent endpoints
// functions 

Working with Buffers -> also under the hood bufio is implementing io package
bytes.Buffer
bufio Package

// along the way understood type conversions since many packages implements io and its interfaces
//questions on when to use different io packages

                            io PACKAGE                              bufio Package              
PURPOSE             Basic interfaces and functions          Buffered I/O operaitons to improve efficiency
                    for IO operations                       by reducing number of system calls

Core Interfaces     Core Interfaces: io.Reader ,            Core Types: bufio.Reader , bufio.Writer, 
/Types              io.Writer , io.Closer ,io.Seeker        bufio.Scanner // bufio does not have interfaces but types

Common Use cases    Direct I/O Operations, Simple Data      Buffered Reading/Writing , line by line reading
                    Transfer , Pipes io.copy                Chunked Reading

Unique Use Cases    Abstract I/O ,Simple Data manipulation  Efficient I/O Operations , Complex Tokenization

