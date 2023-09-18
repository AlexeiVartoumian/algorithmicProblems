"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""

"""
when dealing with prefix sum problems it typicaly involves manipulations of runningsums and for problems involving subarrays storing these running sums in dictionaries for later referencing to solve for a linear solution. As such the problem statement is variation asking for a continous subarray sum such that the product is a mulitpile of k and the lnegth is greater than two. another way of saying this is is my running sum % k equal to zero? and is the index at which this happened greater than than two ? as such the dictionary for referencing will store the remainder as key, as in have i seen this multiple before and the index as value. whenever the remainder reoccurs all thats left to do is see the the currentindex minus the value stored is less than or equal to two.
"""

def checksubarraysum(nums,k):

    records = {0:-1} # where -1 is to represent the beginning index of the array.

    runningremainder = 0
    for i in range(len(nums)):

        runningremainder+= nums[i]

        if (runningremainder % k) in records:

            if i - records[runningremainder%k] >=2:
                return True
        
        else:
            records[runningremainder%k] = i
    return False