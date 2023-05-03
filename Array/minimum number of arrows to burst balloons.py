"""
here are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
"""
"""
the observation  to be made here is that to target the maximal amount of balloons
you should target the upper end of the smallest interval with the lower end of the largest interval SUCH that there is overlap between them meaning if there were three balloons the first lies between point 0 and 3 the second between 1 and 4 and the last between 3 and 9. you only need one arrow because if you shoot at point x = 3 there is overlap between all ballons.

as such what needs to be done is to first sort the intervals in ascending order from the second element of each pair. after that the way I approached this was to
grab the intersection of each interval that respects the above i.e
if there is overlap between larger el of prev interval and smaller el of cur interval continue along interval array until no longer the case in which case just increment and append the higher end of prev interval. the number of times this happens is the minimal number of arrows needed
"""


class Solution:
    def findMinArrowShots( points) :
        points.sort(key = lambda x: x[1])
        intersections = []
        i= 0
        j= 0
        while j < len(points):
            if points[i][1] >= points[j][0]:

                cur = points[i][1]
                while j < len(points) and cur >= points[j][0]:
                    j+=1
                intersections.append(cur)
                i= j
                j+=1
            else:
                intersections.append(points[i][1])
                i+=1
                j+=1
        if points[-1][0] > intersections[-1]:
            intersections.append(points[-1][0])
        return len(intersections)