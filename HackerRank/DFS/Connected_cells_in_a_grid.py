"""
Consider a matrix where each cell contains either 0 a  or a 1 and any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the diagram below, the two colored regions show cells connected to the filled cells. Black on white are not connected.

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.
Complete the function maxRegion in the editor below. It must return an integer value, the size of the largest region.

maxRegion has the following parameter(s):

grid: a two dimensional array of integers

1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output

5
"""

"""
this is a multi-directional depth first search where the whenever a 1 is encountered go in 8 directions asking the questions
is the next co-ordinate in  bounds? have I not visted it before? and is it a one? if all the answers are yes then add it is connected.
uswe a set to avoid visiting the same 1's again and again. finally loop through the entire grid applying above process whenever an unvisited
one has occured.
"""

def maxRegion(grid):
    # Write your code here
    height = len(grid)
    width = len(grid[0])
    visited = set()
   
    directions= [(1,0),(1,1),(0,1),(-1,1),(-1,0), (-1,-1),(0,-1),(1,-1)]
    maxsofar = 0
    def dfs(i,j,visited,val):
        
        if i >= 0 and i < height and j >= 0 and j < width and (i,j) not in visited and grid[i][j] == 1:
            val[0]+=1
            visited.add((i,j))
            for d in directions:
                xcord = i + d[0]
                ycord = j + d[1]
                dfs(xcord,ycord,visited,val)
        return val
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1 and (i,j) not in visited:
                temp = 0    
                temp += dfs(i,j,visited,[0])[0]
                maxsofar = max(temp,maxsofar)
    
    return maxsofar