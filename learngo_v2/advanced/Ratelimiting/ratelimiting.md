
ratelimiting

why use rate limiting
- implements fairness and prevents abuse/overload of resources and cost management ofnetwork communincation

common rate limiting algorithms
- token bucket algorithm - allows bursts of traffic whilst mainting steady rate over time
- leaky bucket algorithm - similar to above but fixed leak rate , it smooths out bursts of traffix 
- fixed window counter - counts requests within fixed time limit until further requests are below limit thundering herd problem
- sliding window log - provides more precise rate limiting then fixed window but needs more memomry
- sliding window counter - adjusts count based on sliding window . 



practical use cases
- api rate limiting
- traffic shaping
- preventing abuse
- load management
