
"""
Given an amount and the denominations of coins available, determine how many ways change can be made for amount. There is a limitless supply of each coin type.

Example
n = 3
c = 8,3,1,2
there are 3 ways to make change for n = 3
{1,1,1}, {1,2},{3}

Complete the getWays function in the editor below.

getWays has the following parameter(s):

int n: the amount to make change for
int c[m]: the available coin denominations
"""

"""
the brute force way to solve this is to make a decision tree for every coin iterating through rest of list where until the target has not been reached
you call the function on itself and pass the current sum and the amended list back into the function and keep doing so until value has been reached do this for all coins.
the way I think solving of solving this dynamically is to state an invariable. given a single coin there is only way to make that value.
we can also say that all multiples of that value will also have that single coin as way to generate that value. those multiples are composed of that value. the value itself can be formed from other coins. for example you have coins: 2 and 1 and the target value is 5. using only coin value 1 there is one way to make change for 1 , 1 way to make change for 2 and so on all the way up to 5.  we know there is only one way to make change with coin val 2 for value 2 . its upon reaching the value three where things get interesting. we already stated there is one way to make change with coin value 1.building on this when we reach a number the question to ask is the current value a composite value such that its something I've seen before if I subtract the current coin. if that value that i've seen before is itself a composite value then I can say all the ways to make that value PLUS the current coin is the number of ways to make change for that coin. in the case value is three and coin is two then three minus two is one is a value that i've sen before. three is a composite value and therefore given coins 1 and 2 there are two ways to make change for three.
As such maintain a records array of n+1 where the zero term is 1 . this represents the invariable coin - coin : there is one way to make change for that value. then for every coin ask the question is cur value minus coin a composite ive seen before? is so then increment number of ways to make change. return the last value of records that symbolizes the target value.    
"""
def getWays(n, c):
    # Write your code here
    values = [0]* (n+1)
    values[0] = 1
    c.sort()
    
    for coin in c:
        for i in range(1, n+1):
            if i -coin >= 0 and values[i - coin] != 0:
                values[i] += values[i-coin]
    return values[n]