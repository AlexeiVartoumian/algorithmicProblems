
collection of remote methods that can be called by clients
essential for structuring apps and are defined with protocol buffers 

we can think of the rpcs as endpoints where the rpc call itself is what is being executed

syntax = "proto3";

package greeting;


service Greeter {
    rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest {
    string name = 1;
  
}

message HelloResponse {
    string conf_message = 1;
}

