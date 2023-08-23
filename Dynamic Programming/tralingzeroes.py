
"""
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
"""

"""
the first observation to make is that every time the number 5 appears a extra is appending to a given factorial sum. as such the idea is to imagine n factorial as a number and consistently divide it by the exponential of 5 that grows each time by a factor of 5. to compute the number of trailing zeroes we take n as a number and the number of trailing zeroes will be n// 5 where 5 is an exponent groinwing by 5. keep doing until n  is 0 
"""

def trailingzeroes(n):
    if n <5:
        return 0

    
    output = 0

    exponent = 5
    while n//5 >0:
        output += n//exponent
        exponent*=5
    
    return exponent