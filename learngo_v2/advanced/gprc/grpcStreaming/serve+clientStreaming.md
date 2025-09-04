SERVER
Send: strean.Send(<Response>) returns Error
Recieve: stream.Recv() returns Request and Error
stream.SendAndClose(<Response>) send response when closing the stream

Client
Send: stream.Send(<Request>) returns Error
stream.CloseAndRecv(<Response>) receive response thenclose the stream
Recieve: stream.Recv() returns Response and Error

RPC Parameter type: pb.<ServiceName>_<RPCName> Server

* int grpc server side streaming ther is no specific method to close the stream .
the server will stop sending messages when it has finsihe3d processing

in grpc client side strweaming the client is repsonsible for closing the stream explicitly after it has finished sending 
messages to the server that is done by using methods associated with the stream to close the stresm