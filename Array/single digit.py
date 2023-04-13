"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

"""
very elegant solution by XORING all the way through we can only ever get
the unique number since XOR is one or the other but not both.
consider the array [2,2,1]. the integer 2 in three bit binary can be expressed as 010. by going through the numbers and XORING with 0 that is 000 we fill always 
get the first number so in this case 001. the next number is also two. two XORED with two is 010 ^ 010. one or the other but not both leaves us with 000. finally
we have the integer 1 (which is 2 to the power of 0 ) which in three bit binary is 001. 000 XORED with 001 is 001. leaving us with the unqiue number.
"""
def singleNumber(nums):

        res = 0
        for n in nums:
            res = n ^ res
        return res