"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
Example 1:
Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
Example 2:
Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.
Example 3:
Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 
Constraints:

2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
Each pair of cities has at most one road connecting them.
"""

"""
the question is basically asking us for the maximum of degree of one node plus another node with the caveat that we cannot count the same pair twice.

as such the idea is to make an adjacency list where for each node we add the nodes it is adjacent too in a SET. since the task is to find the maximum degree we use a comparison loop to pair off unique combinations of each node
and compute the maximum network rank , whci would be  the length of the two sets combined subtracting all instances of the other node in current set. compare this value with current maximum and return when finished.
"""

from collections import defaultdict
def maximumnetworkrank(n,roads):

    adjlist= defaultdict(set)

    for i in range(len(roads)):
        adjlist[roads[i][0]].add(roads[i][1])
        adjlist[roads[i][1]].add(roads[i][0])

    maximal = 0

    for i in range(n-1):
        for j in range(i+1,n):

            maximal = max( maximal, len(adjlist[i]) + len(adjlist[j])- (j in adjlist[i]))
    
    return maximal







def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        """
        idea is to make a default dictionary with a set. then do a comparison loop at every turn
        computing the the maximal length between amximal length and the len of both sets combined minus 
        any connections of i+1 inside the prev adlist list node
        """

        adjlist= defaultdict(set)

        for i in range(len(roads)):
            adjlist[roads[i][0]].add(roads[i][1])
            adjlist[roads[i][1]].add(roads[i][0])
        
        maximal = 0

        for i in range(n-1):

            for j in range(i+1, n):
                maximal = max( maximal, (len(adjlist[i]) + len(adjlist[j]) - (j in adjlist[i])))
               
        return maximal