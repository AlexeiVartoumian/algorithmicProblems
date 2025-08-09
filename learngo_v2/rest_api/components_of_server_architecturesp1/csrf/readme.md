Csrf

- cross- site request forgery
- stateless nature
- token based authentication
csrf exploits trust a web app has in broswer


apis use tokens like jwt for authentication since token is needed for each request

best practices
- use smae site cookies
- double submit cookies
- custom headers
- csrf tokens

common pitfalls
ignoring stateless apis
weak token generation
exposing tokens

primarily needed for applications where server and client have a trust relationship 
and where client performs staechanign operations 
ig a pure api based backend that does not interact with browser then csrf is mitigated

if api does not cookies to authenticate but relies on headers then csrf attacks exploit automatic inclusion of cookies in requests.

non-browser clients wont automatically include credentials like broswers do .
