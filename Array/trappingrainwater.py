
"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


"""
the intuition is to go forwards and then backwards
we only ever record a "pool" of water if the two points holding the 
water are equal to each other at which instance we add that
to the maximum sum. then the two new points are reconsidered and the
above proc is repeated. to handle the edge case where a beginning point
is higher than all other points we also need to go backwards and repeat 
this process so the our rule catches hidden possible pools.
we store actual pools in a dictionary with thier beginnung index as key
with value of running sum as value. check if running sum is stored.
if not then a pool has been missed
"""


class Solution:
    def trap(self, height: List[int]) -> int:

        pools= {}

        highpoint = 0
        runningsum = 0
        begin = 0

        for i in range(len(height)):
            if height[i] >0:
                begin= i
                highpoint = height[begin]
                break
    
        for i  in range(begin+1,len(height)):
            
            if height[i] >= highpoint:    
                if runningsum:
                    pools[begin] = runningsum
                begin = i
                highpoint= height[begin]
                runningsum = 0
            else:
                runningsum+= highpoint - height[i]
        
        begin = 0
        runningsum = 0
        highpoint = 0
        for j in range(len(height)-1,-1,-1):
            if height[j] >0 :
                begin = j
                highpoint = height[j]
                break
        
        for j in range(begin-1,-1,-1):

            if height[j]>= highpoint:
                if runningsum and j not in pools:
                    pools[j] = runningsum
                begin = j
                highpoint = height[j]
                runningsum = 0
            else:
                runningsum+= highpoint - height[j]
        
        maxsofar = 0
        for i,x in pools.items():
            maxsofar+= x
        return maxsofar