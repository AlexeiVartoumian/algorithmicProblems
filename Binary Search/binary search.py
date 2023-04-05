"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
"""
my version at the bottom the classical verison is directly below
"""

def search(nums, target):
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        
        return -1    






def search(nums, target):

        if nums[0] == nums[-1] and nums[0] != target:
            return -1
        elif  nums[0] == target:
            return 0
        elif nums[-1] == target:
            return len(nums)-1  
        
        low = 0
        high = len(nums)-1

        while low < high-1:
            mid = int((low+high)/2)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid 
            else:
                low = mid
        
        return -1
