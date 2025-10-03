
from collections import defaultdict

def queensAttack(n, k, r_q, c_q, obstacles):

    directions = [(-1,0), (-1,1), (0,1) ,(1,1) ,(1,0) ,(1,-1) , (0,-1) , (-1,-1)]

    #for each obstacle generate tuple and store them in set.
    # then for each direction starting from queen position ask if you have seen this before if not continue

    boundx = 0
    boundy = n
    seen =   set()
    numsquares = 0
    for i in range(len(obstacles)):
        xcord , ycord = obstacles[i]
        seen.add((xcord , ycord))

    for d in directions:
        xcord , ycord = d
        dx = r_q
        dy = c_q 
        while (dx + xcord >0 and  dx + xcord <= n ) and (dy + ycord >0 and  dy + ycord <= n ) :
            
            dx += xcord
            dy += ycord
            if (dx , dy) in seen:
                break
            numsquares+=1
    return numsquares

# print( queensAttack(5 , 3 , 4,3 ,[ [4 ,2] , [2 ,3]]))
# print( queensAttack(4 , 0 , 4,4 ,[ ]))





