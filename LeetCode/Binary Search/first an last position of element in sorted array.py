"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
"""
Saw way simpler implementations that what i have but my approach
was to bin search with modification. for minimum first find the target. once found set if the previous val
is not the same as target then minimum has been found. else set the higher bound to current index and perform another
binary search until mid value -1 is not target. the same idea but in reverse for highest value. finally return the function
result in an array 
"""

def searchRange(nums, target):
        def findmin(nums,target):
            low = 0
            high = len(nums)-1
            if nums[low] == target:
                return 0
            while low <= high:
                mid = int((low+high)/2)
        
                if nums[mid] == target:
                    if nums[mid-1] != target:
                        return mid
                    high = mid-1
                    while low <= high:
                        mid = int((low+high)/2)
                        if nums[mid] == target and nums[mid-1] != target:
                            return mid
                        if nums[mid] != target:
                            low = mid+1
                        else:
                            high = mid-1
                if nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1
        def findmax(nums,target):
            low = 0
            high = len(nums)-1
            if nums[high] == target:
                return high
            while low <= high:
                mid = int((low+high)/2)
        
                if nums[mid] == target:
                    if nums[mid+1] != target:
                        return mid
                    low = mid
                    while low <= high:
                        mid = int((low+high)/2)
                        if nums[mid] == target and nums[mid+1] != target:
                            return mid
                        if nums[mid]!= target:
                            high = mid-1
                        else:
                            low = mid+1
                if nums[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return -1

        if not nums:
            return [-1,-1]
        return [findmin(nums,target),findmax(nums,target)]