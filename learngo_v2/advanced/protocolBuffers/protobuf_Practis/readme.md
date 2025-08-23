

once protbuf compiler is installed and for go 
the protofbuf0go gen-go
and and protofugbuv gen-grpx

and the paths are in place on the env varibales can do

protoc --go_out=. main.proto

the syntax has to be veeeeery specific but if all goes well the above command will generate the corresponding go code.

it will inherit the fields specified in the porto file