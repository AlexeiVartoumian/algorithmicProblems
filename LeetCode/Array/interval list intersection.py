"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
 
Example 1:

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
"""
"""
the goal here is to grab the intersections. we do so by computing the maimum of th efirst element first lsit and second list and the minu of the second element of the first list and second list.then its a case of appending the value pair such that start is less than or equal to end. To account  for the end of one list being equal to another list we use a while loop with two iterators i and j , i iterates through firstlist and j iterates through secondlist. they only incremnet if the second element of one pair is smaller the the other , increment through that list
"""

def intervalintersect(A,B):

    i,j = 0,0

    res= []

    while i < len(A) and j < len(B):
        start = max(A[i][0],B[j][0])
        end = min(A[i][1],B[j][1])

        if start <= end:
            res.append([start,end])
        
        if A[i][1]<B[j][1]:
            i+=1
        else:
            j+=1
    
    return res

def intervalIntersection(firstList, secondList):

        i,j = 0,0
        res= []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0],secondList[j][0])
            end = min(firstList[i][1],secondList[j][1])

            if start <= end:
                res.append([start,end])
            
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        
        return res