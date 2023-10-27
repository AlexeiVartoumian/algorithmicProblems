"""You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
"""

from collections import deque

"""
My attempt was the one at the bottom which is basically dfs the first one you come across mark all adjacent 1's as part of that island set. then
go through the rest of matrix and and any other 1 encountered is part of island 2. finally do bfs on the shorter list. it worked but I dont why the time limit exceeded on my attempt sure i have more operations like looping thorugh shorter set and adding it to a queue but thats it really. below solution basically is the exact same approach.
"""


def thingy(A):
        row,col = len(A),len(A[0])
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]
        island1 =deque()
        def dfs(x,y):
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and A[x+dx][y+dy]==1:
                    A[x+dx][y+dy]=2
                    island1.append([x+dx,y+dy])
                    dfs(x+dx,y+dy)
        #DFS Find the first island and turn all 1 to 2
        def findIsland1():
            for x in range(row):
                for y in range(col):
                    if A[x][y]:
                        return dfs(x,y)
        findIsland1()
        #BFS Expand the island and count step
        step = 0
        while island1:
            for _ in range(len(island1)):
                x,y=island1.popleft()
                for dx,dy in dirs:
                    nx,ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col and A[nx][ny]!=2:
                        if A[nx][ny] == 0:
                            A[nx][ny]=2
                            island1.append([nx,ny])
                        elif A[nx][ny] == 1:
                            return step
            step+=1
        return step

class Solution:
    def shortestBridge(self, grid):

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        height = len(grid)
        width = len(grid[0])
        dist = 0
        island1 = set()
        island2 = set()
        counted = False
        def anisland(i,j,island):
            if i >=0 and i <height and j < width and j >= 0 and grid[i][j] == 1 and (i,j,0) not in island:
                island.add((i,j,0))
                for d in directions:
                    anisland(i+d[0],j+d[1],island)
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i,j,0) not in island1 and (i,j,0) not in island2:
                    if (i,j,0) not in island1 and not counted:
                        anisland(i,j,island1)
                        counted = True
                    else:
                        island2.add((i,j,0))
        queue = deque()
        otherisle = None
        if len(island1) > len(island2):
            for i in island2:
                queue.append(i)
        
            otherisle = island1
        else:
            for i in island1:
                queue.append(i)
            otherisle = island2
        zerovisit = set()
        while queue:
            cur = queue.popleft()
            xcord = cur[0]
            ycord = cur[1]
            dist = cur[2]
            for d in directions:
                newx = xcord + d[0]
                newy = ycord + d[1]
                if newx >=0 and newx < height and newy >=0 and newy < width:
                
                    if grid[newx][newy] == 0 and (newx,newy) not in zerovisit:
                        zerovisit.add((i,j))
                        queue.append([newx,newy,dist+1])
                    elif grid[newx][newy] == 1:
                        if (newx,newy,0) in otherisle:
                            return dist
                        else:
                            continue