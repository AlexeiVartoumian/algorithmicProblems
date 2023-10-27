"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

"""
first an observation has to be made, at the beginning of the array, the smallest possible i value is the starting value. we can say that all the previous value before this one no longer matter since you will not have a triplet such that i<j<k.
this means that to find a triplet you will always find one starting from the smallest value in the list if such triplet exists. As such initialise a variable minimum and first set it to infinity.
After making this observation only another pointer is needed and an if elif else statemetn will determine the rest. also set  a second variable like minimum to infinity .if a number is not smaller than minimum but it is smaller or equal to the j variable then set the j variable to that value. 
this will also handle the instance where there only two numbers in the list. finally if a given number is not smaller than the minumum and its GREATER THAN J VARIABle we can return right away since we have found a triplet such i<j<k and each value is greater than the next.
"""

def increasing(nums):

    minimum, j = float("inf"),float("inf")

    for number in nums:
        if number < minimum:
            minimum = number
        elif j >= number: # if we hit here it means we have a middle value
            j = number
        else: # means current number is greater than minimum and middle value.
            return True
    return False