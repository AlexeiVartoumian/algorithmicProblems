
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