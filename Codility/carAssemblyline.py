"""

• There are two assembly lines, each with n stations, for manufacturing some product.

• The time required at station i is not necessarily the same in both assembly lines.

• There is a time cost to switching between assembly lines.

Example:
# A = [1,6,2]
# B = [3,2,5]

# X = 2
# Y = 1

In above example, there are three stations on each line, the time to get from the entry to line 1 and line 2 are e1 and e2 respectively. The time to do work at stations 1, 2 and 3 of both line 1 are line 2 are shown (i.e. a11, a21, etc.). The time to transfer from line 1 to line 2 between stations 1 and 2 is t11, etc.,(similarly for line 2) and the time to get from station 3 to the exit from line 1 and line 2 are x1 and x2 respectively.

Problem:
What is the fastest way to assemble the product (to get from the entry to the exit)? OR What stations should be chosen from line 1 and which from line 2 in order to minimize the total time through the factory for one car?
"""
"""
At first I thought that dijsktras was the way to go but then I went about this by using the built in heapq structure. this is a super cool strucutre that represents a tree like structure but within the array itself where the continuous insertion and deletion of elements is especially suited for when the highest or lowest element is needed every time. this is the case here , because both arrays are of the same length and I framed this as a graph problem where each node/index is connected in a directed fashion to either the element in front of it in either list , ; the heap structure allows for the continous processing of the smallest value node. its in this fashion that visiting the last node of either array will guarantee the cost incurred to get to that node as being the smallest.
"""
from collections import defaultdict
from collections import deque
import heapq
A =[1,6,2]
B = [3,2,5]
X = 2
Y = 1

def smallestpath(A,B,X,Y):

    adja = defaultdict(list)
    adjb = defaultdict(list)

    for i in range(len(A)-1):
        adja[i].append( ( A[i+1] , B[i+1] + X ) )
        adjb[i].append( ( A[i+1] + Y , B[i+1] ) )
        
    adja[len(A)-1].append((-1,-1))
    adjb[len(B)-1].append((-1,-1))
    queue = [(A[0],0, "A")] 
    queue.append((B[0],0, "B"))  
    heapq.heapify(queue)
    while queue:
      
        curcost , index , flag = heapq.heappop(queue)
        traverse = None
       
        if index == len(adja)-1:
            
            return curcost
        if flag == "A":   
            traverse = adja
        else:
            traverse = adjb
        nextcost1  = traverse[index][0][0]
        nextcost2 = traverse[index][0][1]
        
        if index+1 <= len(adja):
            heapq.heappush(queue,(nextcost1 + curcost , index+1 , "A") )
            heapq.heappush(queue, (nextcost2 + curcost , index+1 , "B") )
         
print(smallestpath(A,B,X,Y))


        


