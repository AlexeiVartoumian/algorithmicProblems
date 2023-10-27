"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

""" I used bfs for every direction iteratively.  You should applu the right approacj to the right situation and learn in more detail Depth first search. a more opitmal solution is directyly below and at the very bottom is my own solution"""
grids = [["1","1","1","1","1","0","1","1","1","1"],
         ["0","1","1","0","1","1","1","0","1","1"],
         ["1","0","1","0","1","1","0","1","0","1"],
         ["1","0","1","1","0","1","1","1","1","1"],
         ["1","1","0","0","1","1","1","1","1","1"],
         ["1","1","0","1","1","1","1","1","1","1"],
         ["1","1","1","1","1","1","1","1","0","1"],
         ["0","1","1","0","1","1","1","1","1","0"],
         ["1","1","0","1","1","0","1","1","1","1"],
         ["0","1","1","1","1","1","0","1","1","1"]]

def numIslands( grid) :
        rs, cs = len(grid), len(grid[0]) #rs == rows cs = columns
        def dfs(r: int, c: int): # depth first search is used as a helper function
            if r < 0 or r >= rs or c < 0 or c >= cs or grid[r][c] != '1': # check the boundaries of matrix as a base case
                return
            grid[r][c] = 'X'  # mark as visited
            dfs(r - 1, c) # go left
            dfs(r, c - 1) # go up
            dfs(r, c + 1)# go down
            dfs(r + 1, c)# go right
        islands = 0
        #if at any point there are you have traversed an entire island , you would stil need to loop over 
        #the rest of the matrix incrementing number of islands whenever a one occurs.
        for r in range(rs):
            for c in range(cs):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        return islands


def numIslands(grid):

        visited = []
        if len(grid) == 1:
            total = 0
            if int(grid[0][0]) == 1:
                total+=1
            for i in range(1,len(grid[0])):
                if int(grid[0][i]) == 1 and int(grid[0][i-1]) == 0:
                    total+=1
            return total
        for i in range(len(grid)):
            
            length = len(grid[i])
            
            visited.append([-1]*length)
        
        numberofislands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if int(grid[i][j]) == 1 and visited[i][j] ==-1 :
                    cur = 0
                    #print("starting point", (i,j))
                    component = [(i,j)]
                    row = i
                    col = j
                    visited[row][col]= 2
                    numberofislands+=1
                    while cur < len(component):

                        #right
                        for w in range(col, len(grid[i])):
                            if visited[row][w] == -1 and int(grid[row][w]) == 1:
                                visited[row][w] =2    
                                component.append((row,w))
                            elif visited[row][w] == 0: break
                            elif visited[row][w] == -1 and int(grid[row][w]) == 0:
                               
                                visited[row][w] = 0
                                break
                        #down
                        for x in range(row, len(grid)):
                            if visited[x][col] == -1 and int(grid[x][col]) == 1:
                                visited[x][col] = 2
                                component.append((x,col))
                            elif visited[x][col] == 0: break
                            elif visited[x][col] == -1 and int(grid[x][col]) == 0:
                                visited[x][col] = 0
                                break
                        #left
                        for y in range(col, -1, -1):
                            if visited[row][y] == -1 and int(grid[row][y]) == 1:
                                visited[row][y] = 2
                                component.append((row,y))
                            elif visited[row][y] == 0: break
                            elif visited[row][y] == -1 and int(grid[row][y]) == 0:
                                visited[row][y] = 0
                                break
                        #up
                        for z in range(row, -1, -1):
                            if visited[z][col] == -1 and int(grid[z][col]) ==1:
                                visited[z][col] = 2
                                component.append((z,col))
                            elif visited[z][col] == 0: break
                            elif visited[z][col] == -1 and int(grid[z][col]) ==0:
                                visited[z][col] = 0
                                break
                        cur+=1
                        
                        if cur== len(component):
                            print(component, len(component), i , j)
                            print("checkpoint",visited)
                            cur = 0
                            component = []
                            break
                        else:
                            #print("component so far" ,component)
                            #print("now we start at this point",(component[cur][0],component[cur][1]) )
                            row = component[cur][0]
                            col = component[cur][1]
                            component.pop(0)
                            cur-=1
                            
                            
                elif int(grid[i][j]) == 0 and visited[i][j] == -1:
                    
                    visited[i][j] = 0
        #print(visited)
        #print("and the result is",numberofislands)
        return numberofislands

numIslands(grids)
