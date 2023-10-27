"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Example 1:
Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
Example 2:

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
"""
"""
fuuuuuuuuuuuuuucccckkk!!!
"""


from collections import defaultdict

def isBipartite(graph):

        flip = False
        blue = set()
        red = set()
        visited = set()
       
        adjlist = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjlist[i].append(graph[i][j])
        
        def dfs(prevnode,curnode,red,blue,flip,visited):

            if prevnode == None:
                red.add(curnode)
                flip= True
            else:
                if flip:
                    blue.add(curnode)
                    flip = False
                else:
                    red.add(curnode)
                    flip = True
                if curnode in visited:
                    return
            visited.add(curnode)
            for i in graph[curnode]:
                dfs(curnode,i,red,blue,flip,visited)

        for i in range(len(graph)):
            if i not in visited:
                dfs(None,i,red,blue,flip,visited)
        
        
        for i in range(len(graph)):
            if i in red and i in blue:
                return False
        return True


#below doesnt work and i dont fucking know why. arrrrrrrrrrrrrrrgh!!!!!!!!!!!!!
def isBipartite(graph) :

        flip = False

        blue = set()
        red = set()
        visited = set()
        isBipartite = True
        adjlist = defaultdict(list)

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjlist[i].append(graph[i][j])
        
        def dfs(prevnode,curnode,flip,blue,red,visited,isBipartite):

            if prevnode== None:
                red.add(curnode)
                flip = True
            else:
                if flip:
                    blue.add(curnode)
                    flip = False
                    
                else:
                    red.add(curnode)
                    flip= True
                    
                if prevnode in red and curnode in red:
                    isBipartite = False
                if prevnode in blue and curnode in blue:
                    isBipartite = False
            
            visited.add(curnode)

            for i in graph[curnode]:
                if i not in visited:
                    dfs(curnode,i,flip,blue,red,visited,isBipartite)
                else:
                    if i in red and curnode in red:
                        isBipartite = False
                    if i in blue and curnode in blue:
                        isBipartite = False

            return isBipartite
               
         
        for i in range(len(graph)):

            if i not in visited:

                if not dfs(None,i,visited,blue,red,visited,isBipartite):
                    return False
        
        return True