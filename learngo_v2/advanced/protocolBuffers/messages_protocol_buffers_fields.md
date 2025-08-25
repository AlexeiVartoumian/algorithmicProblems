
messages are core data structures in protocol buffers

what is a message ?
logical container with structured data

they are comproised of fields which are the fundamental building blocks of protocol buffers

<field_type><field_name>=<field_number>;

field Options
in proto2 fields could be marked as required or optional  in proto3 all fields are optional by default

user repeated to define a field that can contain multiple values fo the same type
there are additional values such as default packed and more

FIELD NUMBERS 
-> use numbers between 1 and 15 for frequently used fields as theserequire only one byte in the binary encoding
-> use numbers between 16 and 2047 for less frequently used fields


best practise
use meaningful names
avoid chaing field numbers once assigned


assiging unique field numbersin a message 
- each field in a message is assigned a unique field unumber used interanlly for serialization and deserialization .
they help to maintian backward and forward compatability 

reserved keyword
- used to mark field numbers or names as unavailable for future yse . helps to maintain backwards compatability