

grpc is open source rpc framework .


generating grpc code please refer to protocol buffers section to see how to install protoc 

protoc --go_out=. --go-grpc_out=. proto/main.proto 

the above command wil generated the code into seprate files for the messages and another for the rpc and services


users http2 for transport and protocol buffers as interface 

provides features including auth and load balanncing

can multiplex multiple requests over a single connection

uses protocal buffers to define structure of message and ensuring type safety


simplified overview
services are defiend and its methods with .proto file
then protoc compiler will generate from the .proto file

then the methods of the server methods are implmented server side to handle incoming requests
- define the service
- generate the code
- implement the server
- create the client

supports various stypes of streaming server streaming , client streaming bi-directional streaming

use cases for gRPC
-microserves
- real-time applications
- mobile and iot applications