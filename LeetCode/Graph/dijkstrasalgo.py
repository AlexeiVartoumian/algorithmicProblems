"""
this is not really a leetcode question per se, this is just for fun and to  practise my understanding of this algorithm which i implemented by thinking of an analogy of distances between cities . Dijkstras algo is used when we wish to compute the shortest path from a starting node a given node, to all other nodes in respect to the starting node. by shortest path we mean the distance between two nodes that is represented by as a positive weight. it useful to think of this as the time to travel from city A to City B where the time on the road is the weight of the edge and the road itself is the edge.

to begin we need a distances table where the key is the is the a given node and the value is the distance. these observations can be made. a starting node will have zero distance to itself and we should represent this as a zero in the the distance table. before computing the shortest distance we can assume it takes infinite time to get there as we have not yet found out the shortest path to that city from the starting node.
and the third observation. consider the simplest case where there are three cities 1, 2 ,3. Each city is connected to each other like so

        1
  20  /   \ 5
     /     \
    2---5---3

starting from say city 1 in the simplest case if we visit all the cities that it is connected to, at least one of them IS CERTAIN to be the shortest path to that city. If im not wrong I believe this is the inductive rule and also why this algo cannot work when there exist negative weights. As such I see dijsktra algo as a modification of breadth first search we at every turn we ask what is the smallest distance from starting node to the current node? we use the distance table for reference. at the first pass this will be set to infinity. therefore the crucial and beautiful point of this algo is to ask hey what is smaller the current distance stored in the table to visit the next city or the current city + the distance to get to the next city. 
Once all edges are visited the mark the first traversed city as visited to avoid repeated work. at every step where you make the above computation we also ask the question hey have we visited the next city as in have we applied the above algo to all of its neighbours? if not then add it to the queue inn a breadth first manner. below is the code as i understand it.  
"""

from collections import deque
#here i represent cities as keys, where the values are an array of tuples. each tuple contains the city as first index and the distance as second index with respect to the key value of the dictionary eg : 1:[(2,5)] = city 1 is connected to city with a distance of 5
graph ={1:[(2,5),(7,3),(3,13)],
        2:[(1,5),(3,6)],
        3:[(1,13),(2,6),(4,2),(6,8)],
        4:[(3,2),(6,12),(5,4)],
        5:[(4,4),(6,3)],
        6:[(4,12),(5,3),(7,2)],
        7:[(1,3),(6,2)]
}
def dijkstra(graph,startnode):
    
    distances={}
    
    for i in range(1,len(graph)+1):
        if i == startnode:
            distances[i] = 0
        else:
            distances[i] = float("inf")
    visited =set()
    
    queue = deque()
    queue.append(startnode)
    while queue:
        traverse = len(queue)
        for i in range(traverse):
            curnode = queue.popleft()
            for j in range(len(graph[curnode])):
                nextnode,dist = graph[curnode][j] # dist short for distance
                
                distances[nextnode] = min(distances[curnode]+dist,distances[nextnode])
                
                if nextnode not in visited:
                    queue.append(nextnode)
            visited.add(curnode)
    return distances
                     
dijkstra(graph,4)