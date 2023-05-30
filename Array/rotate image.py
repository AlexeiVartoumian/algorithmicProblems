"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

"""
I died on this question, when the answer is on the tip of your tongue you see the pattern and the relationship but you cannot express it. thats what you get for not knowing linear algebra. mathematically all that needs to be done is transpose the matrix which is reversing the matrix arrays, and then swapping the values contained
looping from all elements of first array on outer loop to all elements up to current iteration of outerloop.
"""

class Solution:
    def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j] ,matrix[j][i] = matrix[j][i],matrix[i][j]