
basic structure of a .proto file

syntax = "proto3";
package example;
//message definition
message Person{
    string name = 1
    int32 id = 2;
    string email =3
}

syntax -> declares syntax version i.e proto3 has improvements over proto2
package -> namespace for the generatd code 
message -> used to defined a structured data type . in example above a message called person has been defined

defineing fields in a message syntax i.e refer to above
<field_type> <field_name> = <field_number>;

basic field Types
int32 , int64 : signed intgers of varying sized
unit32 , uint64 unsigned integers
float , double : floating-point numbers
bool: boolean values
string: a sequence of characters
bytes : a sequence of raw byetes 

in proto3 all fields are optional by default 

field options repeated fields , requires and options
 - message Person {
    repeated string phone_numbers = 1;  -> will be a list of phone nubers
 }

 can comment proto files with //

 enumerations
 enum Gender {
    MALE = 0;
    FEMALE =1;
    OTHER = 2
 }

 Nested message
 message Address {
    string street = 1;
    string city =2;
 }
 message Person{
    string name = 1;
    Address address = 2;
 }