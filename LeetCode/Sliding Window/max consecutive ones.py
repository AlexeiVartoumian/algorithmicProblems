"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

"""
sliding window. the important thing to observe is that we only care about the number of zeroes in our window such that it is always less than or equal to k. as such my approach was to be greedy keeping count of number of zeroes from left to right. whenever a zero is encountered decrement k. when that hits goes below zero keep moving left until the first zero is seen in which case k becomes zero and we can greedily choose the largest window. whenver k is above or eqal to zero compute the maximum between current length and right - left +1.
"""

def maxones(nums, k):

    kzeroes = k
    left = 0

    length = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            kzeroes-=1
        
        if kzeroes == -1:
            while kzeroes == -1:
                if nums[left] == 0:
                    kzeroes+=1
                left+=1
        
        if kzeroes >= 0:
            length = max(length,right-left+1) # careful to account for zero index
        
    return length

def longestOnes(self, nums: List[int], k: int) -> int:

        length = 0

        left = 0
        kzero = k
        for right in range(len(nums)):

            if nums[right] ==0:
                kzero -=1
            
            if kzero == -1:

                while kzero == -1:
                    if nums[left] == 0:
                        kzero+=1
                    left+=1
            if kzero >= 0:
                length= max(length,right-left+1)
                
        return length