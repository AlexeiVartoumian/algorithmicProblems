

serialisation is the process of converting a go object into a json string

json string is a byteslice 

deserialzation is the opposite

go provides two priamary ways of doing this with json marshal and json unmarshal

used for in-memory json processing and are a great use case for situations where
data needs to be quickly deseiralized and deserialized in memory

then is also json decoder and encoder

use case for is for large data sets , or working with network nconnections or large files 

for example streaming data from a network connection or a file 