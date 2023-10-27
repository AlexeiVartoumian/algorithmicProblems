"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

 

Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
"""
"""
breadth first search will compute the shortest distance in an m X n array.
our condition to find is the case where we havwe managed to travese the boundary of the matrix and going in any orthogonal direction makes us go out of bound if this co-oridnate is not the starting point return distance which is stored alongside each cordinate in the queue. if queue finishes return -1.
"""

from collections import deque
def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        height = len(maze)
        width = len(maze[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        queue = deque()
        queue.append([entrance[0],entrance[1],0])
        visited.add((entrance[0],entrance[1]))
        while queue:
            
            cur = queue.popleft()
            xcord = cur[0]
            ycord = cur[1]
            dist = cur[2]
            for d in directions:
                newx = d[0] + xcord
                newy = d[1] + ycord
                if newx >= 0 and newx < height and newy >= 0 and newy < width:
                    if maze[newx][newy] == "+":
                        continue
                    else:
                        if (newx,newy) not in visited:
                            queue.append([newx,newy,dist+1])
                            visited.add((newx,newy))
                else: 
                    if [xcord,ycord] != entrance:
                        return dist
            
        return -1