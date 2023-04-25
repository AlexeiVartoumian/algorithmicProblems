"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 
Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 
"""
"""
The solution below checked out as 10 times more efficient that the one that i implemented 
"""

from collections import Counter

class Solution:
    def exist(self, board, word):
        
        R = len(board)
        C = len(board[0])
        
        # if len of word is greater than total number of character in board
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        # count of a LETTER in word is Greater than count of it being in board
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        # if count of 1st letter of Word(A) is Greater than that of Last One in Board(B). 
        # Reverse Search the word then search as less case will be searched.
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
                        
        # simple backtracking 
        seen = set()    # so we dont access the element again
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C or word[i] != board[r][c] or (r,c) in seen:
                return False
            
            seen.add((r,c))
            res = (
                dfs(r+1,c,i+1) or 
                dfs(r-1,c,i+1) or
                dfs(r,c+1,i+1) or
                dfs(r,c-1,i+1) 
            )
            seen.remove((r,c))  #backtracking

            return res
        
        for i in range(R):
            for j in range(C):
                if dfs(i,j,0):
                    return True
        return False


def exist(self, board, word):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        currentstring = ""
        height = len(board)
        width = len(board[0])
        array = []
        visited = set()
        def dfs(i,j,currentstring,count):
        
            if count == len(word):
                array.append(currentstring)
            elif i < height and i >=0 and j < width and j >= 0 and board[i][j]==word[count] and (i,j) not in visited:
                count+=1
                currentstring+= board[i][j]
                visited.add((i,j))
                for d in directions:
                    dfs(i+d[0],j+d[1],currentstring,count)
                visited.remove((i,j))
        
    
        for i in range(height):
            for j in range(width):
                if board[i][j] == word[0]:
                    currentstring = ""
                    visited = set()
                    count = 0
                    dfs(i,j,currentstring,count)
    
    
        for i in range(len(array)):
            if array[i] == word:
                return True
        return False