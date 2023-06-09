"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

def findMaxAverage(self, nums: List[int], k: int) -> float:


        left = 0
        right = k
        runningsum= 0
        avgvalue = 0
        
        for i in range(k):
            runningsum+= nums[i]
        
        avgvalue = runningsum/k

        for j in range (right, len(nums)):
            runningsum+=nums[j]
            runningsum-=nums[left]

            avgvalue = max(avgvalue, runningsum/k)
            left+=1
        
        return avgvalue
