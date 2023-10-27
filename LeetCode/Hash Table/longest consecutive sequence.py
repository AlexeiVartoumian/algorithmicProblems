"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""

"""
firstly create a set so that we will only have unique numbvers to check and avoid duplicate work i.e a number list like[0,0,0,0,0,0,0,0,0,0,0,4,3,2,1]. after this two passes of the set will be required. on the first apass we store all the numbers from our set in the hashmap.
then we make  a second pass of the numbers with the following intention. for any given number in the set we check if the preceding number as in (number -1) is stored in the  dictionary. if this is not the case THEN THAT GIVEN NUMBER IS THE START OF SUBSEQUENCE. as such have a inner loop with an iterable number set to our starting number that iterates until iterable is not in dicitonary. compare largest consectutive numbers.
"""

def consecutivenumbeers(nums):

    if not nums:
        return 0

    nums = set(nums)

    curlargest = 1
    theobject = {}
    for i in nums:
        theobject[i] = 1
    
    for i in nums:
        if i-1 not in theobject:

            temp = 1 #compare this val with curlargest
            iterable = i+1
            while iterable in theobject:
                temp+=1
                iterable+=1
            curlargest = max(curlargest,temp)

    return curlargest

def longestConsecutive(self, nums: List[int]) -> int:
        
        
        if not nums: return 0

        theobject = {}

        nums = set(nums)
        for  i in nums:
            theobject[i] = 1
        
        curlargest =1

        for i in nums:
            if i-1 not in theobject:
                temp = 1
                iterable = i+1
                while iterable in theobject:
                    temp+=1
                    iterable+=1
                curlargest = max(curlargest,temp)
        
        return curlargest

