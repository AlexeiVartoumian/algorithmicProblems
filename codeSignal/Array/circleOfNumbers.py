"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.
"""
"""
at first I thought this would require some rotational operation but n is an integer. as such given a number if it  less than n //2 thad add n//2 to that number otherwise subtract.
"""

def solution(n, firstNumber):
    
    
    if firstNumber < (n//2):
        firstNumber += n//2
    else:
        firstNumber -= n//2
    
    return firstNumber