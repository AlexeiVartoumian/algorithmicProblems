"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
"""
"""
the to keep in mind is that we want the first instance where the list is no longer ascending. the only thing to watch out
for is when mid and low become the same value because we are explicitly looking for value at current index -1 to be greater then current index
"""
def findMin(nums):
        if len(nums) ==1:
            return nums[0]
        if nums[0] < nums[-1]:
        #do normal bin search
            return nums[0]
    
    
        lowpoint = nums[0]
        highpoint= nums[-1]
        low = 0 
        high = len(nums)-1
        while lowpoint > highpoint:
            mid = int((low+high)/2)
            if nums[mid] < nums[mid-1]:
                return nums[mid]
        
            if nums[mid] >= lowpoint:
                if low == mid:
                    low = mid+1
                else:
                    low = mid
            else:
                high = mid+1