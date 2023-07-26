"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""
"""
have two dictionarys , one for column and one for rows where the key for both will be index and value will be that respective array, which will be either across or down. once genereated all that has to be done is to loop through either of the dictionaries and for each record, check if it exists in the other dictionary. if so increment result, when finished return result.
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows ={}
        cols ={}

        for i in range(len(grid)):
            rows[i] = grid[i]
            column = []
            for j in range(len(grid[i])):
                column.append(grid[j][i])
            cols[i] = column
        
        res = 0
        for i ,x in cols.items():

            for i in range(len(grid)):
                if x == rows[i]:
                    res+=1
        return res