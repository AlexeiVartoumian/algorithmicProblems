"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

"""
The way i did it was incredibly inefficient but I went for dfs with orgthoganol directions. I had to be careful not to overwrite or underwrite any elements that were orthongoanlly adjacenet so the approach is so.
loop through and mark all orginal zeroes. then do the same again only this time mutate the matrix making sure to not add any original zeroes to visited. after that mutate and repeat in the orginal loop.

the way more efficient solution is to mark all the zeroes in a two sets i and j and then loop again without dfs mutating if a given element is not equal to zero and is in the row or column of matrix.
"""


def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited = set()

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        zeroes = set()

        height = len(matrix)
        width = len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    zeroes.add((i,j))

        def dfs(i,j,visited,matrix,d1,d2):

            if i < height and i >= 0 and j < width and j >= 0 and (i,j) not in zeroes:
                visited.add((i,j))
                matrix[i][j] = 0
                newx = i + d1
                newy =j + d2
                dfs(newx,newy,visited,matrix,d1,d2)

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    visited.add((i,j))
                    
                    for d in directions:
                        newx = i + d[0]
                        newy = j + d[1]
                        dfs(newx,newy,visited,matrix,d[0],d[1])

def setZeroes( matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        row_set = set()
        col_set = set()

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        

        for row_index in row_set:
            for j in range(cols):
                matrix[row_index][j] = 0
        
        for col_index in col_set:
            for i in range(rows):
                matrix[i][col_index] = 0
        