"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]

Output: [     [0,0,0],
              [0,1,0],
              [0,0,0]]
Example 2:
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]

Output: [     [0,0,0],
              [0,1,0],
              [1,2,1]]
"""

"""
Since this question is asking for the distances of every 1 relative to the closest zero adjacent to it the way to approach this problem is to use breadth first search. The idea is to have four auxilary data strucutures by name of visited, queue , directions and answer. visited will be a set where we will store unique indexes so as not to traverse them again, with the added benfit that looking up a elemnt in a set takes constant time.
queue will be a double ended queue where the length of it at a given iteration will determine the relative distance to a zero. directions will be a set of four co-ordinates which will enable the traversal to move orthogonally. and finally answer will be a copy of the intitail grid, ony it will be populated with 0's to be evetntually filled with ones.

As such the procedure is as follows. 
step 1: loop through the entire grid. whenever a zero is encountered add it to both the queue and visited data structure. this is for the purpose of finding the nearest 1's to a respective zero, where each zero will be at respective points of the grid.

step 2:  set distance to zero and initiliase a while loop that will keep running until the queue is empty. the initial length of the queue will be all the zeroes inside of the matrix. 
pop the leftmost value of the queue and store the i index and j index in respective variables. 

step3: check if the i and j variables in the grid are a 1. if so then set the answer structure (which is a near copy of the orginal grid) to distance variable. remember this works because on the initial iteration all the values in the queue are zeroes. that means if a queue value is a one we have popped all the zero values and new 1 values in the queue are going to be the distance to a zero , which is determined by the length of the queue.

step4: loop through the directions where horizontal is equal to i + d[0] and vertical = j + d[1]. check if horizontal and vertical repsect the boundaries of the grid and wether they are unique as in they have not occured in visited.
if this is the case then add this value to both the queue and visited.

step 5: repeat the above process until the initial length of the queue is finished. remember on the first iteration all the values will be zeroes.
the new length of the queue will be the closest ones found to each zero. iincrease the distance variable by one. if we encounter any 1 variables that are adjacent to another one but not adjacent to another zero then they will be appended to the queue in step 4. when the second version length of the queue is finished the distance variable will increase again.

finally when there are no more elemnts inside of the queue we have visited every index of the grid and the updated answer grid is all the distances of 1's relative to the clossest zero.
"""
from collections import deque
"""
        [0,0,0]
        [0,1,0]
        [1,2,1]
"""

agrid = [[0,0,0],
         [0,1,0],
         [1,1,1],
         ]
def matrix(grid):

    height = len(grid)
    width = len(grid[0])

    visited = set()
    queue = deque()
    ans = [[0]* width for _ in range(height)]

    directions= [(1,0),(0,1),(-1,0),(0,-1)]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                queue.append((i,j))
                visited.add((i,j))
    dist = 0
    while queue:

        
        for x in range(len(queue)):

            thing = queue.popleft()
            i = thing[0]
            j = thing[1]

            if grid[i][j] == 1:
                ans[i][j] = dist
            
            for d in directions:

                horizontal = d[0]+ i
                vertical = d[1]+ j

                if 0<= horizontal< height and 0<= vertical< width and (horizontal,vertical) not in visited:
                    queue.append((horizontal,vertical))
                    visited.add((horizontal,vertical))
        
        dist+=1
    return ans
            
print(matrix(agrid))         
    



                


"""
def matrix(grid): 
    
    height = len(grid)-1
    width = len(grid[0])-1
    first = True
    for i in range(len(grid)):
        for j in range(len(grid)):
            
            if grid[i][j] == 0:
                d = [[1,0],[0,1],[-1,0],[0,-1]]
                dist = 1
                queue = deque()
                queue.append((i,j))
                visited = []
                
                for n in range(len(grid)):
                    temp= []
                    for m in range(len(grid[0])):
                        temp.append(-1)
                    visited.append(temp)
                track = None
                visited[i][j] = 1
                while queue:
                    if track == None:
                        track = queue[0]
                    c = queue.popleft()
                    level = []
                    for n in range(len(d)):
                       
                        if c[0]+ d[n][0] > height or c[0]+ d[n][0] <0 or c[1]+ d[n][1] >width or c[1]+ d[n][1] < 0 :
                            continue
                        
                        else:
                            if grid[c[0]+ d[n][0]][c[1]+ d[n][1]] == 0:
                                visited[c[0]+ d[n][0]][c[1]+ d[n][1]] = 1
                            elif visited[c[0]+ d[n][0]][c[1]+ d[n][1]]== -1:
                                queue.append((c[0]+ d[n][0],c[1]+ d[n][1]))
                                level.append((c[0]+ d[n][0],c[1]+ d[n][1]))
                                if first:
                                    grid[c[0]+ d[n][0]][c[1]+ d[n][1]] = dist
                                else:
                                    grid[c[0]+ d[n][0]][c[1]+ d[n][1]] = min(grid[c[0]+ d[n][0]][c[1]+ d[n][1]],dist)
                                visited[c[0]+ d[n][0]][c[1]+ d[n][1]] = 1
                        print(queue ," is now")
                    if c == track:
                        dist+=1
                        if queue:
                            track = queue[-1]
                first = False                   
matrix(agrid)
"""           
            
        
