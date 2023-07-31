"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

"""
so there appears to be numerous ways of solving this , of course theer is the elegant dunamic programming approach where the result is bubbled up or down in a computing the min distance every time, since at base case a given index can only bre reached from the one directly above or to the left. I was learning about dijkstras algorithm today and I attempted to implemnt my understanding of it on this problem. my approach was as follows: since the matrix itself is can be seen as an adjacency matrix with the value inside being the weight it costs to travel from either the node directly above it if it exists or the node directly to the left if it exists (since from starting node only possible to traverse right or down) I would keep a distance table  and visit all adjacent nodes , adding to queue only if they are present in the unvisited set for queue once all adjacent nodes of a current node in the queue have been visited then add that to the visited set. at every turn compute wether the smaller distance between current value stored in distance table and the currnet not plus  
"""

def minPathSum( grid):

        visited = set()
        distance = {}
        directions = [(1,0),(0,1)]
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        notvisited = set()
        for i in range(height):
            for j in range(width):
                if i == 0 and j ==0:
                    distance[(i,j)] = grid[i][j]
                else:
                    distance[(i,j)] = float("inf")
                    notvisited.add((i,j))
        queue.append((0,0))
        visited.add((0,0))
        while queue:
            curnode = queue.popleft()
            i,j = curnode[0],curnode[1]

            for d in directions:
                down = i+d[0]
                across = j + d[1]
                if down >=0 and down < height and across >=0 and across <width:
                    if ((down,across) not in visited) and (down,across) in notvisited:
                        notvisited.remove((down,across))
                        queue.append((down,across))
                    distance[(down,across)] = min(distance[(down,across)],distance[(i,j)]+ grid[down][across])
            visited.add((i,j))
        return distance[(height-1,width-1)]