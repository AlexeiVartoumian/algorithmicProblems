"""
Given an array of integers nums and an integer k, determine whether there are two distinct indices i and j in the array where nums[i] = nums[j] and the absolute difference between i and j is less than or equal to k.

Example

For nums = [0, 1, 2, 3, 5, 2] and k = 3, the output should be
solution(nums, k) = true.

There are two 2s in nums, and the absolute difference between their positions is exactly 3.

For nums = [0, 1, 2, 3, 5, 2] and k = 2, the output should be
solution(nums, k) = false.

The absolute difference between the positions of the two 2s is 3, which is more than k.
"""
"""
the thing to keep in mind is that there may be more than two instances of a number. other than that store the number as key and the index it occured as value as part of a list. loop through the list whenever number occurs chekcing if curindex minus given index <=k.
"""

from collections import defaultdict
def solution(nums, k):
    
    
    theobject = defaultdict(list)
    
    for i in range(len(nums)):
        
        if nums[i] in theobject:
            
            for j in theobject[nums[i]]:
                if abs(i - j) <= k:
                    return True
      
        theobject[nums[i]].append(i)
    return False
