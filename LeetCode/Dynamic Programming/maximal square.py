"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:

Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
"""

thing =[["0","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0"],
        ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
        ["1","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1"],
        ["1","0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0"],
        ["0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1"],
        ["1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],
        ["0","1","1","0","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0","1"],
        ["1","1","1","1","1","1","1","1","0","1","1","0","1","1","0","1","1","1","1"],
        ["1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","0","1","1","1"]]

"""
my implementation of a dynamic progrmaming approach. you break down the problem into its most basic component. in this case what makes a square?
in the first instance a 1 by 1 will be a square. the key is the next smallest possible square. the rule is this. for a two by two square to be a square the bottom right value has to have the bottom left , top left and top right values as 1 and it needs to be 1 as well. in other words given a sqaure of one by one for it to be a two by two swuare all the adjacent elements of the right , bottom and bottom right need to be 1. as such the appraocj is to "bubble down" the value . for every element we want tograb the minimum of diagonal left element, top and left  and store it in the current element. check if next bottom, bottom right and right are all 1. if so then increment current value by 1. keep track of largest square found so far with a maximum so far variable.
"""
def maximalSquare(matrix):

        height = len(matrix)
        width = len(matrix[0])
        maxsofar=  0
        for i in range(height):
            for j in range(width):
                if int(matrix[i][j]) != 0:
                    if i-1 >=0 and j-1 >= 0: # check if prev elements of cur are in bounds
                        prevsquare = min(int(matrix[i-1][j-1]),int(matrix[i][j-1]),int(matrix[i-1][j]))
                        if prevsquare: # if not zero then next possible largest square can only be the prev smallest since we want a true square, not rectangle
                            matrix[i][j] =prevsquare
                        else:
                            matrix[i][j] = int(matrix[i][j])
                    else:
                        matrix[i][j] = int(matrix[i][j])
                    # not compute the bottom, bottom right and bottom right if all 1's then increment cur element by 1
                    if i+1 < height and j+1 < width:
                            a = int(matrix[i+1][j])
                            b = int(matrix[i][j+1])
                            c = int(matrix[i+1][j+1])
                            calculate = min(a,b,c)+1
                            if calculate == 2:
                                matrix[i][j]+=1
                            else:
                                 matrix[i][j] = 1
                    maxsofar = max(maxsofar,matrix[i][j])
        
        squareval = maxsofar*maxsofar
        return squareval
print(maximalSquare(thing))
