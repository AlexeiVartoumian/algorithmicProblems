"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.
You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
Example 1:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:
Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
"""

"""
I thought I could just use a process of elimnation and use a single pass ; if a BOTH in a visited pair have been visited before then I have an additional cable to use and the number of unconnected computers left will be the number of cables I needed -1. this does not take into account however that a disconnected computer does not have to be in isolation , it can be disconnected from other computers. as such the solution I finally came up with was this. intitalise an object with a node as the key and array as value. for every pair value append the opposite value to the object key to signify it is connected. then have a visited array of lnegth n. after this use depth first search on each key in the object. if its possible to visit every node on the first go then return the number needed -1 to represent 1 cable mapping to two computers.
"""

def makeConnected(n,connections):

            
        if len(connections) < n-1 :
            return -1
        visited = [0] * n
    

        theobject = {}
        for x in range(n):
            theobject[x] = [] 
        for i in range(len(connections)):

            if connections[i][0] not in theobject[connections[i][1]]:
                theobject[connections[i][1]].append(connections[i][0])
            
            if connections[i][1] not in theobject[connections[i][0]]:
                theobject[connections[i][0]].append(connections[i][1])
        
        numberneeded = 0

        def dfs(i,visited):
            if visited[i]== 0:
                visited[i] = 1
                for j in range(len(theobject[i])):
                    if visited[theobject[i][j]] == 0:
                        dfs(theobject[i][j],visited)

        for i in range(len(visited)):
            if visited[i] == 0:
                dfs(i,visited)
                numberneeded+=1
        return numberneeded-1