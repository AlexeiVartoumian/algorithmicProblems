

once protbuf compiler is installed and for go 
the protofbuf go gen-go
and and protobuf gen-grpc

and the paths are in place on the env varibales can do

protoc --go_out=. main.proto

as well as using multip; proto files . please note that inside the proto file
option go_package = "some/dir" will influence where the pb file will be generated eg 
option go_package = "/proto/gen;mainwithservicepb"; declared in proto file iwll creater it theres 


protoc -I=. --go_out=. main.proto user/user.proto order.proto

breaking the above down -> 
protoc = command
-I= the directoro to execute in . in this case the current directory specified as -I=. 
--go_out=.  = generate the pb files for go
finally the proto files where they are located


note there are extenstions for 

the syntax has to be veeeeery specific but if all goes well the above command will generate and compile the corresponding go code.

it will inherit the fields specified in the porto file

when the proto file is generated with the rpc serivce specified
we can see a number of things 
i.e the HelloRequest struct has a field Name and Age of tupe protobuf as well as json.

additionally the struct has fields like state , sizeCache and uknownFields which were generated.
They are lowevercase which means they are prviate fields.

there are also getters and setters on the generated functions.

grpc uses http2 where http2 compresses the data with gunzip present int he generated protocal buffer files

rpc are nothing but functions and messages are basically the arguments that are recieved for a function 
or the outputs


