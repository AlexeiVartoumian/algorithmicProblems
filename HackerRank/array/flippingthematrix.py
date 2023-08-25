"""
Sean invented a game involving a 2nX2n matrix where each cell of the matrix contains an integer. He can reverse any of its rows or columns any number of times. The goal of the game is to maximize the sum of the elements in the  submatrix located in the upper-left quadrant of the matrix.

Given the initial configurations for  matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.
"""


matrix = [
    [112,42,83,119],
    [56,125,56,49],
    [17,78,101,43],
    [62,98,114,108]]
"""
given the constraints where we are only allowed to reverse a given column 
or reverse a given row, the most important observation here is that for any given element in the matrix only 4 possible values can be live at that element.
for example at position (0,0) there can only be (0,3) --> reversing the row
(3,0) by reversing the column and (3,3) by reversing the column and then reversing the row, which is 4 possible positions including the original element. since we only care about the upper left quadrant and the matrix is 2n by 2n we use a double loop that both iterate to half the length of matrix
at the first pass add the highest value between the four possible elements that can be in that position. we getting the maximal value between (i j) co-ords at orignal position ,  ( len(matrix) -i-1 , len(matrix) - j -1 ) which is basically the far bottom possible value where the sum of co-ords will be highest and then a mix of the above to grab the corresponding horizontal value and corresponding vertical value. as I and j increase the our upper and lower bounds decrease essentially targeting the other required 3 possible values that can exist in the upper left quadrant. keep adding the maximal value finally returning the sum when done. 
"""

def flipthematrix(matrix):

    maximalsum= 0
    for i in range(len(matrix)//2):#we only care about upper left quadrant
        for j in range(len(matrix)//2):

            maximalsum+= max(matrix[i][j], matrix[i][len(matrix)-j-1], matrix[len(matrix)-i-1][j],matrix[len(matrix)-i-1][len(matrix)-j-1])
    return maximalsum


