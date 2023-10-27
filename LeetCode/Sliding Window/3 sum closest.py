"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""

"""
the first thing to do is to sort the list. after that as you iterate through the list the idea is to use two pointers where you check every possible combination of sums. leftpointer will be one ahead of current iteration and right pointer will always start at the end of list. if at any point the  absoltute value of target minus current sum is smaller than  absolute value of target minus clostst then set closest to this. if the current sum is equal to target return right away. otherwiste if current sum is larger than decrement rightpointer by one. if its smaller than current sum then increment by one. do this while leftpointer is smaller than right pointer. repeat for whole loop. return closest sum
"""

def closestsum(nums,target):

    closest = (10**8) # set it to a arbitrarily large number

    nums.sort()
    # dont go up to lastg two numbers to account for comparisons
    for i in range(len(nums)-2):
        leftpointer = i+1
        rightpointer = len(nums)-1

        while leftpointer < rightpointer:
            cursum = nums[i] + nums[leftpointer]+ nums[rightpointer]

            if cursum == target:
                return cursum
            if abs(target - cursum) < abs(target - closest):
                closest = cursum
            
            if cursum > target:
                rightpointer-=1
            elif cursum < target:
                leftpointer +=1
    
    return closest

class Solution:
    def threeSumClosest(nums, target):
 

        nums.sort()
        closest = (10**8)
        for i in range(len(nums)-2):

            leftpointer = i+1
            rightpointer = len(nums)-1

            while leftpointer < rightpointer:
                cursum = nums[i] + nums[leftpointer]+ nums[rightpointer]
                if cursum == target:
                    return cursum
                if abs(target - cursum) < abs(target - closest):
                    closest = cursum
                
                if cursum > target:
                    rightpointer -=1
                elif cursum < target:
                    leftpointer+=1
        
        return closest