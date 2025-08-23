on the topic of data serializations

protocol buffers known as protbuf

data serializations is process of converted structured data into a format that can be easily transmitted 
serialization -> process of converting a data strucuture or object into a byte stream
deserialization -> reverse process of serilization

what are they ? 
language agnostic binary serialization format , ideal for ntrnasmission over netowrk

key features 
- efficiency -> smaller footprint then kjson or text files
- speed -> 
- crossplatofrm compatibility designed for multiple languages

Use cases
- microservices communication -> often used to transmit between services 
ensuring minimal overhead for high performance capability
- enable strong typing ensuring data format
- dtata storage
- game developement


how they work
define data structure ina dot proto file and 
the protoc compiler generates source code in various languages

first define message in proto file then use protoc compiler to generate code in target language
then creae instance of message and populate fields then serialize which is done by code created by protoc compiler
then serialized byte slice can be stored or sent over the network . then deserialized in the same way by protoc compiler


advantages
can evelve data structureswithout breaking existing implemntations
enforce strict typing
support many languages
exceelent choice for microservices and api's
less verbose then json or xml smaller then text data 
