"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""

"""
traverse te graph keeping track of vistied nodes.all rooms must be possible to be visited from room zero else return false.
compare length of visited nodes to number of indexes in array.
"""

def canVisitAllRooms(self, rooms) -> bool:

        number = len(rooms)

        visit = set()
        visit.add(0)
        def dfs(i,curvisit):
            
            if i not in curvisit:
                curvisit.add(i)
                for j in rooms[i]:
                    dfs(j,curvisit)

        for i in range(len(rooms[0])):

            curvisit = set()
            dfs(rooms[0][i],curvisit)
            for j in curvisit:
                if j not in visit:
                    visit.add(j)

def canVisitAllRooms(rooms) -> bool:
        visited = set()
        
        # bfs
        queue = [0]
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr not in visited:
                visited.add(curr)
                for adjacent in rooms[curr]:
                    queue.append(adjacent)
            
        return len(visited) == len(rooms)



        return len(visit) == number