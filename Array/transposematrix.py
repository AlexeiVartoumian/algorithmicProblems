"""
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
"""

"""
given an m by n matrix traverse on the main diagonal and swap the elements on that diagnoal.
where for each element we grab the column of the given index diagonal and treat it as our new row. 
if its an mxn matrix we define the number of rows in the transpoisiton as the width of the row[0] (our intial number of columns) and the width of the given row that is the number of columns as our now number of rows in the inital matrix.
"""

def transpose(matrix):

    res = []

    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        res.append(temp)
    return res