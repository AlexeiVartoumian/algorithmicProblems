
"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

Example

The grid is illustrated below.

a b c
a d e
e f g
The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

Function Description

Complete the gridChallenge function in the editor below.

gridChallenge has the following parameter(s):

string grid[n]: an array of strings
Returns

string: either YES or NO
Input Format

The first line contains , the number of testcases.

Each of the next  sets of lines are described as follows:
- The first line contains , the number of rows and columns in the grid.
- The next  lines contains a string of length 

Constraints



Each string consists of lowercase letters in the range ascii[a-z]

Output Format

For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.
"""
"""
as always the prompts from hackerrank are ambiguous giving all test cases as n by n strings even saying "given a square grid" and then in the test cases throwing an n*m. anyway the algo is sort the each index string first as per spec using map
and then onlu loop through the columns to see if ord values are in increasing order.
"""

def gridChallenge(grid):
    # Write your code here
    print("current grid", grid)
    for i in range(len(grid)):
        grid[i] = list (map(str, grid[i]))
        grid[i].sort()
        grid[i] = "".join(grid[i])
        
    
    alpha= True
    
    for i in range(len(grid[0])):
        for j in range(len(grid)-1):
            if ord(grid[j][i]) > ord(grid[j+1][i]):
                
                alpha = False
                break

    if alpha:
       return "YES"
    else:
        return "NO"