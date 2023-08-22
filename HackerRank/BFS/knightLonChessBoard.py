""" is a chess piece that moves in an L shape. We define the possible moves of  as any movement from some position  to some  satisfying either of the following:

 and , or
 and 
Note that  and  allow for the same exact set of movements. For example, the diagram below depicts the possible locations that  or  can move to from its current location at the center of a  chessboard:

image

Observe that for each possible movement, the Knight moves  units in one direction (i.e., horizontal or vertical) and  unit in the perpendicular direction.

Given the value of  for an  chessboard, answer the following question for each  pair where :

What is the minimum number of moves it takes for  to get from position  to position ? If it's not possible for the Knight to reach that destination, the answer is -1 instead.
Then print the answer for each  according to the Output Format specified below.

Input Format

A single integer denoting .

Constraints
"""
"""
    this problem is ambiguous. does the knight have a predetermined moveset or not?
    Im going to assume the explanation is showing how a knight moves on a nx n board
    
    for example if it could only move 1 by 1. if the problem wanted me to compute how to do move for any knight then they should give this as a parameter.
    
    otherwise since the size of the board is the only given i will go ahead
    and compute all possible paths for a traditional knight movement
    (1,2) or (2,1). also the problem does not specify if the knight peice actually behaves like a normal knight because 
    if it did then it would also be able to move in a "negative" direction. the way the problems diagrams only show the knight moving in a positive direction and allowing for only half the knights moves.
    therefore my algo is such
    bfs. given  a starting point compute all possible path with traditional knight move.
    so long as it respects the boundaries of the board. maintain a visted set that keep to avoid repeated work.
    base case is if the square landed on is == (n- 1, n-1) return distance.
very first thing to do is to construct an nx n board.
    """
from collections import deque

def knightlOnAChessboard(n):
    # Write your code here
    
    visited = set() # acccepts (i,j) pairs
    
    board = []
    for i in range(n):
        board.append([0]*n)
    height = n
    width = n
    queue = deque()
    queue.append((0,0,0))
    visited.add((0,0))
    dist = 0
    directions = [[1,2],[2,1]]
    while queue:
        
        traverse = len(queue)
        for x in range(traverse):
            cur = queue.popleft()
            i = cur[0]
            j = cur[1]
            dist = cur[2]
            if i == n-1 and j == n-1 :
                return dist
            for d in directions:
                if i + d[0] < width and j + d[1] <height :
                    if (i+d[0],j+d[1]) not in visited:
                        queue.append((i+d[0],j+d[1],dist+1))
                
    return -1


def check_boundary(r, c, n):
    return 0 <= r < n and 0 <= c < n


def bfs(a, b, n):
    q = deque([(0, 0, 0)])
    dirs = [[a, b], [-a, b], [-a, -b], [a, -b],
            [b, a], [-b, a], [-b, -a], [b, -a]]
    visited = [[False]*n for _ in range(n)]

    visited[0][0] = True
    while q:
        current_r, current_c, depth = q.popleft()

        depth += 1

        for dr, dc in dirs:
            new_r = current_r + dr
            new_c = current_c + dc
            if check_boundary(new_r, new_c, n) and not visited[new_r][new_c]:
                if new_r == n-1 and new_c == n-1:
                    return depth

                q.append((new_r, new_c, depth))
                visited[new_r][new_c] = True

    return -1
