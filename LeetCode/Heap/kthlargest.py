"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

"""
A maxheap! is a tree like structure that is complete binary tree where it can also be arranged into a list. the notation for the list representaion of heap is for every index k
its children are k*2 + 1 and k*2 + 2. as such the goal is to rearange the list of numbers into a maxheap and then to find the kth largest element
all that needs to be done is to use pop the smallest element.
"""
import heapq
class Solution:

    def findKthLargest(self,nums:List[int],k:int) -> int:

        nums = list(map(lambda x:-x,nums)) # python does support max heaps so for every element just turn it into its negative representation
        heapq.heapify(nums) 
        
        for i in range(1,k):
            heapq.heapop(nums) # work up to the kth largest element
        
        return -heapq.heappop(nums) # keep in mind that python only supports minheap so to return the actual kth element return the negative
