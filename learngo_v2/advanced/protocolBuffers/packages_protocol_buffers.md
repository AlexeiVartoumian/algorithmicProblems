


understanding packages is essential for organizating dot proto files and preventing naming conflicts


what are packages
-> a way to define a namespace for messages and enumerations within dot proto file
-> to declare a package name 

package naming conventions
lowercase
dot notation
consistenty 


importing packages

FILE: 
person.proto
syntax = "proto3";
package example;
//Message definition
message Person {
    string name = 1;
    int32 id =2;
}

FILE
main.proto
syntax = "proto3";
package main
//importing another .proto file example
import "example/person.proto";
message Company{
    repeated example.Person employees = 1; // Using the Person message from the example package
}


furthermore using packages ensure that messages contained within them do not conflict 
avoiding naming conflicts
FILE
user.proto
syntax = "proto3";
package user;
message User {
    string username = 1;
}
FILE
admin.proto
syntax = "proto3";
package admin;
message User{
    string adminId = 1;
}

