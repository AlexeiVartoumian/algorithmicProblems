
on wirintg files 

key components 
os components
key functions

Create(name string) (*File , error)
OpenFile(name string , flag int , perm FileMode) (*File , error)
Write(b[]byte)(n int , err error) -> write a byteslice to the file object
WriteString(s string) (n int , err error) -> writestring will write a stirng to the file