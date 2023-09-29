"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
"""
"""
    two loops are required for the first instance I need to check where the mines are and store those co-ordinates inside fo a queue. then in the second loop I use an 8 -directional iteration on every mine and += 1 on every co-ord that is visited.
"""

from collections import deque
def solution(matrix):
    
  
    
 
    visited = set()
    height = len(matrix)
    width = len(matrix[0])
    
    res = []
    res=(list([0]* width for i in range(height)))
    
    directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
   
    queue = deque()
    
    def dfs(i,j):
        
        for d in directions:
                xcord = i + d[0]
                ycord =  j + d[1]
                
                if xcord >= 0 and xcord < height and ycord >= 0 and ycord < width:
                    res[xcord][ycord] +=1
        
    
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == True:
                queue.append((i,j))
    
    
    while queue:
        cur = queue.popleft()
        xcord = cur[0]
        ycord = cur[1]
        dfs(xcord,ycord)    
        
    
    return res