

grpc straming allows clients and servers to send and recieve a strsm of messages
rather than a single reauest and response

userful for continuous data exchange or a or when size of data is too large for single request


types of strwmaing
- server streaming -> upon request server streams messages
- client streaming -> cline sends a streams of requests and server sends single response to taht stream
- bi-directional strwaming -> both client and server communicate 



good for char servicwes or live updates 
good for data as its avialble

when defining serv-side streaming then proto file should define the rpc as stream