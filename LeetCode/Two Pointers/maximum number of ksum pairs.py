"""
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""
"""
I failed hard on this one by overcomplicating. first I thought I needed a two sum dictionary that was dynamically updated. took too long.  then I thought what if i had a pointer to avoid repeated work when a k-sum was found. waaaay to many edge cases. bad bad bad. then finally thought to sort the numbers and
use a right pointer to sum up with current number and exit the loop if right ever met up with left or if left was greater than k . i jankily came up with the generally accepted solution while the cleaner nicer version of what i was trying to do is below my solution.
"""

def maxOperations( nums, k) :


        nums.sort()
        operations = 0
        right = len(nums)-1
        for i in range(len(nums)):

            if nums[i] >= k:
                return operations
            if not nums[i]:
                continue
            
            while right > i:
                if nums[right] and nums[i] + nums[right] < k:
                    break
                
                if nums[right] and nums[i] + nums[right] == k:
                    nums[right] = None
                    operations+=1
                    right = right -1
                    break
                right -=1
            if right == i:
                return operations
        return operations

def maxOperations(nums , k) :
        nums.sort()

        l, r = 0, len(nums) - 1
        moves = 0

        while l < r:
            total = nums[r] + nums[l]
            if total == k:
                moves += 1
                r -= 1
                l += 1
            elif total < k:
                l += 1
            else:
                r -= 1

        return moves  