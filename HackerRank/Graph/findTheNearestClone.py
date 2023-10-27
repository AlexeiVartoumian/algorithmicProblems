"""
In this challenge, there is a connected undirected graph where each of the nodes is a color. Given a color, find the shortest path connecting any two nodes of that color. Each edge has a weight of . If there is not a pair or if the color is not found, print .

For example, given , and  edges  and  and colors for each node are  we can draw the following graph:

image
Each of the nodes is labeled [node]/[color] and is colored appropriately. If we want the shortest path between color , blue, we see there is a direct path between nodes  and . For green, color , we see the path length  from . There is no pair for node  having color , red.

Function Description

Complete the findShortest function in the editor below. It should return an integer representing the length of the shortest path between two nodes of the same color, or  if it is not possible.

findShortest has the following parameter(s):

g_nodes: an integer, the number of nodes
g_from: an array of integers, the start nodes for each edge
g_to: an array of integers, the end nodes for each edge
ids: an array of integers, the color id per node
val: an integer, the id of the color to match
"""
#graph_nodes = 5
#graph_from = [1,2,2,3]
#graph_to = [2,3,4,5]
#ids = [1,2,3,1,3]
#val = 3 ==> 1 val=1 ==> 2 val = 2 ==> -1

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#

"""
this is a bfs question where a few things have to be taken care of before wqe can traverse the graph. as such the way I approached this
question was to first construct a general adjacencylist keeping track of nodes that have the target colour.

once this processing is done all that is left to do is to iterate through the set of target colours and visit all possible nodes
from a given colour. if along the way we see another target colour then add the pathsum to an array of results. conitniue for all target colours. if there are no values in the result return -1 otherwise return the smallest found value.
"""
from collections import defaultdict
from collections import deque
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    adjacencylist = defaultdict(list)
    visited = set()
    correctcolours = set()
    for i in range(len(graph_from)):
        #step 1 add colour to set 
        if ids[graph_from[i]-1] == val and  ids[graph_from[i]-1] :
            correctcolours.add(graph_from[i])
        if ids[graph_to[i]-1] == val and ids[graph_to[i]-1] :
            correctcolours.add(graph_to[i])
        
        adjacencylist[graph_from[i]].append(graph_to[i])
        adjacencylist[graph_to[i]].append(graph_from[i]) 
    
    visited = set()
 
    minpath = -1
    queue = deque()
    routes = []
    for i in correctcolours:
        queue.append(i)
        path = 1
        visited= set()
        visited.add(i)
        notfound = True 
        while queue and notfound:
            traverse = len(queue)
            for j in range(traverse):
                #here we go thorugh the adjcecncy list
                cur = queue.popleft()
                for m in range(len(adjacencylist[cur])):
                    if adjacencylist[cur][m] in correctcolours and  adjacencylist[cur][m] not in visited:
                        routes.append(path)
                        notfound = False
                        queue = deque()
                        break
                    else:   
                        if adjacencylist[cur][m] not in visited:
                            queue.append(adjacencylist[cur][m])
                            visited.add(adjacencylist[cur][m])
            
            path+=1             
    if not routes:
        return -1
    return min(routes)