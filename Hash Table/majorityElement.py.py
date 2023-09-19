
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums) -> int:

        theobject= {}
        curmax = 0
        curnumber = None
        for i in nums:
            theobject[i] = 1 + theobject.get(i,0)
            if theobject[i] > curmax:
                curnumber = i
                curmax = theobject[i]
        
        return curnumber
