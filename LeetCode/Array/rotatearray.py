"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

"""
the approach here is to make a particular observation , in order to roate an array by a given integer k, one has to know the properties of an array, chiefly that they are zero based and are indexed according to the number of elements inside of them. After knowing this, to rotate an array element say the last one of length 7 so element at index 6 and you wish to rotate the element to the right by three it will end up at index two.
to achieve this for every element I derived the formula : (index)+ k % len(array) where three variables , the given index , the amount needed to rotate and the length of the actual array when arranged above will rotate according to specidfication. 
my approach was to keep an auxillary array open and modify the nums array after looping through every element and change its index according to k. directly below does the same but uses string slicing to reverse the string according to the modified position of k
"""

def rotate(nums , k):
        """
        Do not return anything, modify nums in-place instead.
        """
      
        i = k % len(nums)
        nums[:] = nums[-i:]+nums[:-i]

def rotate(nums, k) :
        """
        Do not return anything, modify nums in-place instead.
        """
        #if k = 3 and index = 0 and length of array is 7 then index 0 element needs to be at position 3
        #(index + k) % len(arr)
        # 0 + 3 % 7 = 3 
        switch = [0] * len(nums)
        for i in range(len(nums)):
            switch[(i + k) % len(nums)] = nums[i]
        nums = switch
        