"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.


Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
"""
"""
recursive answer
"""
def isPowerOfTwo(n):
                
       

        if n - int(n) != 0:
                return False
        if n == 1:
            return True
        elif n < 1:
            return False
        n = n/2
            
        return isPowerOfTwo(n)
       