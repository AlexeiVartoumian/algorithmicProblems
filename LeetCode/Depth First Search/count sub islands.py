"""
You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

Example 1:

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
"""
"""
the application of depth first search is done so with the following conditions the basis of which is if it is true for part of the sub island then it must be true for EVERY SUB ISLAND. as such we only ever increment our sub island count if the dfs call on the if condition returns a boolean of true. as such if we encounter a 1 on the first function call we ask , are we out of bounds of the grid? or have we encountered a zero in grid 2 , or have we visited this cooridnate before? if all of those conditions pass then we have exhausted aqll possibilities and return true. 
if one of those conditions fail then it is evident we have a 1 in grid 2 on the current function call. we then ask is there a 1 in the corresponding grid1. if not then the currnent island in grid2 cannot be a subisland of grid 1 and we return False.
ON the first function call the second condition will pass and the first will not , alllowing us to make the directional calls. we assume then that if it is true for one elment in grid2 it is true for all. we set a variable called result to true and mark current element as visited.
WE THEN SET RESULT EQUAL TO A BOOLEAN : RESULT from the previous function call AND DFS(NEW DIRECTION) and do this for all directions keeping in mind if it is true for one element in possible sub island it must be true for all , consequently if it is false for one it must be false for all. when all possbilities have been exhausted finally return res. if it is true then the loop if condition will return true and count can be incremented. visited will avoid repeated work.
"""



def countSubIslands(grid1, grid2) :


        height = len(grid1)
        width = len(grid1[0])

        visited = set()
        count = 0

        def dfs(i,j,visited):

            if i < 0 or i >= height or j <0 or  j>= width or grid2[i][j] == 0 or (i,j) in visited:
                return True
            
            if grid1[i][j] == 0:
                return False
            visited.add((i,j))
            res = True
            res = dfs(i+1,j,visited) and res
            res = dfs(i,j+1,visited) and res
            res = dfs(i-1,j,visited) and res
            res = dfs(i,j-1,visited) and res
            return res
        for i in range(height):
            for j in range(width):

                if grid2[i][j] == 1 and grid1[i][j] == 1 and (i,j) not in visited and dfs(i,j,visited):
                    count+=1
        return count