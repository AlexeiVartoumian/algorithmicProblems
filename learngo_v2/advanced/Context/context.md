what is context

context is a type avaialble form the context package , broadly speaking they are variables that store values,
its not something tahts working in the background its root context for which all other contexts can be derived
its typically used a starting point for creating other contexts . usually created in main funciton or top-level request handlers



USED FOR:
- lifecycle operations 
- to carry deadlines , 
- cancellation singals 
- carry request scoped values
- can amke programm more robust and responsive especially handling long operations network requests and resoruce cleanup

closely associated with api's USED TO MANAGE LIFECYCLE OF PROCESSS AND WHEN operations should be aborted i.e grpc api or rest api request scoped values data across api boundaries . broadly speaking valruables of key value tupe and are integral to making an api

basic concepts
- context creation
    context.Background()
    context.TODO()
- context hierarchy (how contexts are created and derived)
    context.WithCancel()
    context.WithDeadline()
    context.WithTimeout()
    context.WithValue()

crate contexts with context.BaCkground() or context.TODO()
practical usage
-context cancellation
- timeouts and deadlines
-context values

best practiscs
- pass as first parameter for funtions that require it
- avoid stoirng global
- use for request scoped data 
- avoid stoing contexts in structs
- propagating context values
- hadnling context cancellation
- handling context values for 
- avoid creating contexts in loops can cause leaks use single context for entire scope

common pitfalls
- ignoreing context cancellation
- misusing context values ->  vaoid using context to pass optional config/arguements that function parameter can do
