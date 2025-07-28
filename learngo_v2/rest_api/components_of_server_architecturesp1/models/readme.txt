
models are an abstraction layer between database and application logic

and server as documentation to help devs undersatnd structure of data and how they can be undersatnd

proper use can prevent sql injection via sanitization

best practices inlcude 

- avoid putting business logic in models
- simple data scrutcue
- field tags o be used i.e json enconde
- always validate data in system when using models
- the idea is to structure unstrcuted dta

json is a long string and you cannot access the ekys in a json format


best practises for data validation
- There are different types of validation, like checking if the data follows a specified format, for

example, email addresses, phone numbers, etc. then we have presence validation.

That means we ensure that required fields are not empty.

integers for age, strings for names, etc..

Next, we check if the data falls within acceptable ranges.


best practises 
- validate early 
provide clear error messages 
- use libary and frameworks
implement server side validation

common pitfalls
- overly restrictive validation 
- ignoring data types
- inadequate testign 