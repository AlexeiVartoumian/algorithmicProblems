"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
"""
"""
store frequencies as values then iterate through them and add them to set. return true if loop finishes.
"""

def uniqueOccurrences(arr):

        freq = {}
        for i in arr:
            freq[i]  = 1 + freq.get(i,0)

        count = set()
        for i,x in freq.items():
            if x in count:
                return False
            
            count.add(x)
        return True