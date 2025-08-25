
Feature             Rest                Grpc
Architecture        Resource Oriented   Service oriented

Protocol            http1.1 1/2         http/2

data format         json, xml           protocol buffers binray format

Communication style request-response    remote procedure calls

Perofrmance         slower              faster

streaming support   limited             full support

Erorr hadnling      http status codes   grpc status codes

code generation     have to code        generation from .proto


----
key features on rest is its statelessness and 
typically contains all the information needed to fufill a request and server does not store client context.

Uniform Resource Identifiers are used for representation of data which is treated as a resource
clients interact with resources using http methods for example json or xml.
clients can rea3ues specific method.

grpc enables communication between distribured systems and protocol buffers are methods to define service methods and message types.
supports streaming requestr s and responses for real-time apps.

when to use rest over grpc ?
use rest when building a crud api and need to expose resouces to variety of clients

use grpc when high performance and low latency i.e microservices comms or rel time comms or streaming capbalitilies 