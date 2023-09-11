"""
We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range .

Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2
This took three replacements at a cost of .

Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

int s[3][3]: a  array of integers
"""
"""
several observations can be made here
1. no duplicate numbers
2.  which means all numbres must be distinct
3. if all numbers are distinct then all numbers are between 1-9 in a 3 by 3
4. the number 5 must be in the cneter
5. since the total sum of 1- 9 is 45 then the sum of a row must be 15.
6. whatever number is in the diagonal it must be even.
7. whatever number is in the horizontal plane it must be odd.
8. the complement of a given number mys sum to 10.

as such because we are ask3ed to find the minimal cost to form a magic 3x3 square there is only one actual way to do this since all of the properties above can only be true with as a permutation of which there are eight. as such loop thorugh predefined arrays and if a given vlue does not match compute the cost. when done looping theough a given magic square append that cost to a array of costs. finally return the smallest cost which will be the minimal maount of operations to form a magic square.
"""

def formingMagicSquare(s):
    # Write your code here
    
    combinations = [
    [[8,1,6],[3,5,7],[4,9,2]],
    [[6,1,8],[7,5,3],[2,9,4]],
    [[4,9,2],[3,5,7],[8,1,6]],
    [[2,9,4],[7,5,3],[6,1,8]],
    [[8,3,4],[1,5,9],[6,7,2]],
    [[4,3,8],[9,5,1],[2,7,6]],
    [[6,7,2],[1,5,9],[8,3,4]],
    [[2,7,6],[9,5,1],[4,3,8]]]
    
    costs =[]
    for i in range(len(combinations)):
        startcost = 0
        for j in range(len(s)):
            for m in range(len(s)):
                if combinations[j][m] != s[j][m]:
                    startcost+= abs(combinations[i][j][m] - s[j][m])
            
        costs.append(startcost)
    return min(costs)