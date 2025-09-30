
-dedalines and timesouts 
can specify a time limit for a rpc call applied to client side requests

- message compression
can reduce size of messages over the nterwork i.e in rest api used gunzip 

can also use reflection with api testing

also grpc gateway can be exposed as restul apis 

also supports headers + metadta 
wheere 
server -> 
metadata.FRomIncomingContext
- to extract metadata from Client
grpc.SendHEader 
- to send metadat to client

Client
metadata.NEwOutgoingConetxt
- to send metadata to server
grpc.Header
- to extract metadata from server


Trailesrs similar to headers but sent after reponse body  -> can provide additionalo information
also key value response can convey information at a post date not immediately available
i.e processing a status or unique identifier for an operation


09/08/2025 -> saw how using postman with grpc can be done by going on postman file-> new ->  grpc 
where there are a number of protocols to chose from .
from there it was a case of importing the proto file that already generated and running the server. 
if all goes all well i.e no unimplemented method or some other thing then should be able to initiate client server calls using rpc.
also saw doing this dynamically with reflection but not a recommended thing for production


09/12/2025 -> using reflection on the server can use it as a discovery kind of things i.e
querying the server for avialable methods without sharing proto file downloaded grpcurl
.\grpcurl -plaintext localhost:50051 list calculator.Calculator