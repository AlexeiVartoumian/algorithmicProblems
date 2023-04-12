"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
"""

"""
Approach I used was to take a hashtable storing each sum of squares as a value and the previous value as key. if in a new operation a value is already in the table that means we are about to enter a cycle. return false. as soon as 1 occurs then break the while loop and return true.
"""
def isHappy( n) :

        occuring = {}
        thesum= 0
        mutate = str(n)
        while True:
            temp = 0
            for i in mutate:
                temp= int(i) * int(i)
                thesum+= temp
            if thesum == 1:
                return True
            elif n not in occuring:
                occuring[n] = thesum
            else:
                return False
            n = thesum
            mutate = str(n)
            thesum = 0
        return True