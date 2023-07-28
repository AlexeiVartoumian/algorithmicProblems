"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

"""
the intuition behind this one . I intially thought to do a binary search on the sorted input array and avoid iterating through numbers to arrive at an optimal solution but this drove me nuts. instead of doing a binary search on sorted input array you go do a binary search so to speak on the values between 1 and the maximum pile. the idea is that starting at the mid point
you iterate through the entire list and calculate the end hours it takes to eat that that midpoint, the rate of eating bananas if you will. if the number of hours is greater than hours given then the current midpoint is not a fast enough rate and therefore increase the lower bound. however if the current rate is lower or equal to hours then it is known it will that rate to finish.
store the current computation in the final result to be returned which will compare the minimum between cur value inside it(intially set to max) and the cur rate. then decrease the higher bound and do again.
"""
import math
def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()
        low = 1
        high = piles[-1]
        minimum = high
        while low <= high:

            mid = int((low+high)/2)
            hours = 0

            for curpile in piles:
                hours+= math.ceil(curpile/mid)
            
            if hours <= h:
                minimum = min(minimum, mid)
                high = mid-1
            else:
                low = mid+1
        
        return minimum
