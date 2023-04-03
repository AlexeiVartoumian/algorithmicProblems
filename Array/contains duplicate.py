"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
"""
either check if the length of  the set of numbers is less than the length of numbers. if they are the sme length that means every elemetn in nums is unique. the other way to do it is to stoe each value in a dictionary. if any letter is already in the dictionary then you know theres a duplicate inside the array.
"""

def containsDuplicate(nums):

        if len(set(nums)) < len(nums):
            return True
        return False



def containsDuplicate(nums) :
        freq_count = dict()
        for element in nums:
            if element in freq_count.keys():
                return True
            else:
                freq_count[element] = 1
        
        return False    