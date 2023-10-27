"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""
Assuming the matrix is not empty start from position 0,0. Then looping through the required directions right, down,left and up check
if the next position is in bounds of matrix. if not move to next direction. keep doing this until the length of the resulsts appended are equal to the number of elements in the grid. visited is a set variable that makes sure we do not traverse the same element. the inner while loop will keep traeversing in the same direction until the any of the above conditions are not broken.
"""
def spiralOrder(matrix):
        visited = set()
        numberofels = len(matrix) * len(matrix[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)] #right,down.left,up
        res = []
        horizontal = 0
        vertical = 0
        res.append(matrix[horizontal][vertical])
        visited.add((horizontal,vertical))
        while len(res) != numberofels:
            
            for d in directions:
                while True:
                    if  not 0<= horizontal + d[0] <len(matrix):
                        break
                    
                    elif not 0<= vertical + d[1] < len(matrix[0]):
                        break
                    else:
                        if (horizontal+d[0] ,vertical+d[1]) not in visited:
                            horizontal+= d[0]
                            vertical+=d[1]
                            visited.add((horizontal,vertical))
                            res.append(matrix[horizontal][vertical])
                        else:
                            break
        
        print(res)
        
        return res