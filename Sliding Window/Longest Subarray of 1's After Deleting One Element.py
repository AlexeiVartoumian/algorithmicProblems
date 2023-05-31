"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
"""
"""
i fell hard on this question.  need to revisit. eventually came up with a solution where I keep count of zeroes in a given subarray and shift the left pointer until inedx between left and right has zero count of one.
used booleans to handle edge cases where all the digits are 1's or there a longest given subsequence are all ones but there are preceding zeroes in which case delete one fo those zeroes. outside of edge cases as such my approach  was to treat  every subarray with only one zero inside of it as if that zero were a one and to compute the maximum length between maximumlength and currentlength = right index - left index +1.
"""







def longestSubarray(nums) :

        if len(nums)<=1:
            return 0
        
        found =False
        left = 0
        foundzero = False
        for i in range(len(nums)):
            if nums[i] == 1:
                found =True
                left = i
                break
            foundzero = True
        curlen = 1
        flip = False
        right = left
        allones = True
        obj = {}
        zerocount = 0
        while right < len(nums):

            if nums[right] == 0 and flip:
               
                while right < len(nums) and nums[right] == 0:
                    zerocount+=1
                    temp = right
                    right+=1
                if right < len(nums):
                    
                    while zerocount >1:
                        if nums[left] == 0:
                            zerocount-=1
                        left+=1      
            elif nums[right] == 0 and not flip:
                allones = False
                flip = True
                curlen = max(curlen,right-left+1)
                right+=1
                zerocount+=1
            else:
                curlen = max(curlen,(right-left)+1)
                right+=1
        
        if foundzero and allones:
            return curlen
        return curlen-1