

fo rthis  proj assume a contracte is required for a backend sever for a school

school is client 
school management system that admin staff can use to manage students teachers and staff members

project reqs
crud ops
- must add entries on student /teachers/staff/exec
- must modify entries on student /teachers/staff/exec
- must delete on student /teachers/staff/exec
- must list on student /teachers/staff/exec

auth; login logout
bulk modificaiton on student /teachers/staff/exec
class managementL
totoacal count of class with teacher
securit t + rate limiting 
rate lmit app
password reset mechanism
decativeate user

models
Student:
- first name
- last name 
- class -> related to teafcher
- email
Teacher
- first name
- last name
- subject
- class   -> related to student
- email
exceutves
- first name
- last name
- role 
- email
- username
- pasword

common practise 
modulearity -> each endpoint has single repsonsibility
docs -> isntructions on how to use each endpoints documentsing intputs + outputs
error handling -> meaningful error messages + http status codes
testing -> validate inputs , test with variety of cases

