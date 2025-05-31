

care about this pacakge when sending/prcoessing data in chunks


can be used streaming platform , audio 

all about transferring data ebtw4een two ends utlizing small chunks of data

key compononents

bufio.Reader -> is  astruct and rwarpa around 

func NewReader (rd io.Reader) *Reader -> creates new isntance of reader wraps requires a source 
func (r *Reader) Read(p []byte) (n int , err error) -> reads finite amount of data into byte slice
func (r *Reader) ReadString(delim byte) (line string , err error) -> similar when we want to read lines and want to stop at a certain byte/ character eg a newline


bufio.Writer

func NewWriter(wr io.Writer) *Writer
func(w *Writer) Write (p []byte)(n int , err error)
func (w *Writer) WriteString(s string) (n int , err error)


bufio has differences to io packages
bufio provides effcient buffering of datga redung need for system calls
also has convenient methods
bufio wraps around io reader and io writer so errors propogates

best prac
always return errors
wrap reader and writer instances for efficent buffered io operations
dont forget to flush the internal buffer