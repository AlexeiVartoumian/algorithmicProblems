rest api

applicaiton progamming interface
set of rules + protolcs that allow differnet software applicaitons
to communicatre with each other 

rest -> respresentational state transfer

key concecpts 
-statelessnes _. each requ3est must contatin all the information

- client server architecure focuesses on separtions of concerns between client and server

- uniform interface serves to decouple
- resource based each resource is accessd with standard http methods

- stateless communication every request from a client to server must contain all info eg authentication tokens , wquery paramters

cachebility - responses from the server must define if they are cacheable or not
which redueces number of requests and improves performance

from this comes restful api
comppnents of restgul apis 
-resources -> objects + data that api exposes

- resource idenitfies by url
- endpoints specifgic urls where resourcs are accessed

- endpoints are used to either retireve or submit information

- rest apis allow for flexible data formats
eg json , xml

stalessnes simplifies server design , complexity can grow for client side state management

may not be suitable for where real time applicaitons + updates a re reuiqed
