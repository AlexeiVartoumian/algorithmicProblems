"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

"""
if the number is converted to a string then it can be iterated over.
since input is always even split into two and perform calculation taking the integer from of cur index.
"""
def solution(n):
    
    iterable = str(n)
    
    left = iterable[:len(iterable)//2:]
    right = iterable[len(iterable)//2::]
    
    leftsum = 0
    rightsum = 0
    
    for i in range(len(iterable)//2):
        leftsum+= int(left[i])
        rightsum+= int(right[i])
    return leftsum == rightsum