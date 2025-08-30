https://httptoolkit.com/blog/http3-quic-open-source-support-nowhere/
https://medium.com/tech-internals-conf/http-3-shiny-new-thing-or-more-issues-6e4fe14e52ea
generating a self signed cetificate to imple a tls server



generated self-signed certificates using OpenSSL.

however take note that above byitself is incomplete and will error out on dns altnames.
to prevent this use a openssl.cnf file and the below example command for the config file

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout key.pem -out cert.pem -config openssl.cnf

this is for the purpose of simulating a valid certificate authority .

note that in intial connection we may see 
2025/07/20 19:01:54 http: TLS handshake error from [::1]:58334: EOF

which indicates an issue with the CA most likely being self signed. once connection is established though furture requests
would not show this

in prod use certificate from a trusted certificate authority 

But  in development phase.

So we used OpenSSL and we created self-signed certificates.

certificate contains information about isser and details filled out by them

key.pem is the private key for decrypting information 

pem stands for privacy enhanced mail . used for storoing cryptograhic keys certificates

der -> distinguished encodign rules and binary encoding for x509 certificates

pem formatu is base 64 encoded allowing for easier transportation of fules

server uses the pem file to prove its idenity and establish a secrure connection.
and cert is provided to clients to verigy servers idenity and to encurpt the data sent to the server.

in summary are just tex files contingint cryptographic keys and certificates encoded in base 64 
with specific footers and headers 
pem conatins the private key for decryption and cert conatins the the public key and certificate for

-- using curl alongside postman
anatomy of a verbose curl request consider example below

curl -v -k https://10.**.**.**:3000/orders
ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519 / RSASSA-PSS
* ALPN: server accepted h2
* ALPN: server accepted h2
* Server certificate:
*  subject: C=AU; ST=na; L=somewhere; O=org.co; OU=office; CN=coco; emailAddress=test.com
*  start date: Jul 19 19:59:11 2025 GMT
*  expire date: Jul 19 19:59:11 2026 GMT
*  issuer: C=AU; ST=na; L=somewhere; O=org.co; OU=office; CN=coco; emailAddress=test.com
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://10.**.**.**:3000/orders
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: 10.**.**.**:3000]
* [HTTP/2] [1] [:path: /orders]
* [HTTP/2] [1] [user-agent: curl/8.5.0]
* [HTTP/2] [1] [accept: */*]
> GET /orders HTTP/2
> Host: 10.**.**.**:3000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/2 200
< content-type: text/plain; charset=utf-8
< content-length: 24
< date: Sun, 20 Jul 2025 15:20:04 GMT
<
* Connection #0 to host 10.62.30.57 left intact
handling incoming orders

anatomy of a verbose curl request 
otuput
terms
alpn = application layer protocol network
tcp handshake = syncronzied request -> goes to server -> server sends acknowledgement -> then client sends acknowledgement back to server
tls handshake = client sends a message to server with information such as supported ssl / tls versions a ciphersuite

the curl request begins with a tls handshake intiation like so
client sends a request with tls version 1.3 and the server responds with  tls1.3 and a random number at the end
then the server sends the public key which could be the encrypted extension bit.
because the -k flag was used the the step for certifcate validation would be used.
its at this stage an exchange in keys is done.

the client then generates a pre master secret  and encrypts with servers public key that is from the certificate send this pre-master secret to the server.
now both client and server use this pre master secret to generate the same session keys for encryption and decryption.
finally the client and server send a "finished" message to each other with the session keys where there are two finsihed
messages with denoted with (IN) and (OUT).

then the alpn has negotiated to use http2 as the protocol.
for tls connections we can see the three way handshake on and the alpn has accepcted the http2 request from the client
then the server certifcate has been accepted by the client.
afterwhich the certificate details are printed
once the connection is established an session ticket is prescribed where data passing thourgh the ocnnection will be
encrypted with session keys prescribed with a session token demonstrating a persistent connection 
TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):

then it shows the http method and finally the actual response

ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519 / RSASSA-PSS
* ALPN: server accepted h2
* ALPN: server accepted h2
* Server certificate:
*  subject: C=AU; ST=na; L=somewhere; O=org.co; OU=office; CN=coco; emailAddress=test.com
*  start date: Jul 19 19:59:11 2025 GMT
*  expire date: Jul 19 19:59:11 2026 GMT
*  issuer: C=AU; ST=na; L=somewhere; O=org.co; OU=office; CN=coco; emailAddress=test.com
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://10.**.**.**:3000/orders
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: 10.**.**.**:3000]
* [HTTP/2] [1] [:path: /orders]
* [HTTP/2] [1] [user-agent: curl/8.5.0]
* [HTTP/2] [1] [accept: */*]
> GET /orders HTTP/2
> Host: 10.**.**.**:3000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/2 200
< content-type: text/plain; charset=utf-8
< content-length: 24
< date: Sun, 20 Jul 2025 15:20:04 GMT
<
* Connection #0 to host 10.62.30.57 left intact
handling incoming orders

all browsers support http2 with tls only
aka h2 
as can be seen by * ALPN: server accepted h2

additionally grpc requires http2 protocol for transport

because it uses advanced features such as multiplexing streams over a sinlge tcp stram connection to perform efficiently

grpc cxan be used without https but its strognly recommeded to do so

# http1.1 = tcp
uses a model called persistent connections known as keep alive
- a single tcp connection can hanlde multiple requests and responses
- however if presistent connection is left open or not closed a request will open a new connections 

persistent connection allows the server and client to resue the same tcp connection for multiple req+response
reducing overhead of establishing a new connection each time

we can observe this in the headers section where the connections spec is keep alieve

latency is important factor where each connection will create an overhead

sending the above curl request for example is a synchronized curl request from the client which recieves a synchronized response

then there is multiple connections can lead to higher resource consumoption on both client + server side because of need to manage this 

# https (http over tls/ssl)
in tls handshae an addtional step is needed where intial overhead latency wise is needed
but also supports persistent connections meaning multiple requests can be 
sent over the same tls connection after the initail handshake/
there is an overhead in the encryption and decryption process.

# http2 = tcp 
connection behaviour a little differnt uses multiplexing ,
allows multiple streams of data to be sent over a single connection simultaneously 
 - this avoids head of line blcoking seen in http 1.1
 - like http1 typically uses single tcp conection reducing overhead of multiple connections
- supports prioritization of streams meaning more important requests can be processed first 
multiplexing allows for many reusts to be in flight




# http3 = udp 

ssl vs tls
- both cryptographic protocols designed for secure communication
ssl = secure sockets layer
older version of protocol considerred decprecated
tls = transport layer security


mutual tls
 - both the server and the clinet authenticate each other using certificates
 i.e internal comms in microserveices  or secure client server apps
 very specific use-case not practical for example a bank portal that is browser based
 in other words the server will not respond unless the client has the same certificate as our server
