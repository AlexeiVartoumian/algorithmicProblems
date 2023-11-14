"""
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. This means that if a bomb detonates in cell i,j any valid cells (i +1 , j) and (i,j+1)
 are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
After one second, Bomberman does nothing.
After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
Bomberman then repeats steps 3 and 4 indefinitely.

Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment), and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs, determine the state of the grid after N seconds.

For example, if the initial grid looks like:

...
.O.
...
it looks the same after the first second. After the second second, Bomberman has placed all his charges:

OOO
OOO
OOO
At the third second, the bomb in the middle blows up, emptying all surrounding cells:

O.O
...
O.O
"""
"""
Function Description

Complete the bomberMan function in the editory below.

bomberMan has the following parameter(s):

int n: the number of seconds to simulate
string grid[r]: an array of strings that represents the grid
Returns

string[r]: n array of strings that represent the grid in its final state
"""

"""
So i know that the state of the grid will inevitably alternate between three states outside of the first state.
as such I needed to create these states as a grid where I go in orthgonal directions for each "O" I encounter.

the crux of this problem is that the bomberman grid will alternate forever between the 3rd second and the 5th second.
as such anything greater then 3 we can say the following. to find out which term the number n is in as in ....if n is odd does it belong to the
3rd second state or 5th second state. therefore
if n is even return the full field of bombs.
otehrwise find out which term in the sequence n is by dividing it by 4 and rounding up then subtract 1 to get the zero term and mutliplying that by 4 and adding 1 back again to see which odd second grouo it belongs in . 

"""

import math

def bomber(bomb,n):

    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    hieght = len(bomb)
    width = len(bomb[0])

    fullstate = [ "O" * width for i in range(hieght) ]
    states = []
    states.append(bomb)
    states.append(fullstate)

    def grabcoords(bomb):
        coordinates= []
        for i in range(len(bomb)):
            for j in range(len(bomb[0])):
                if bomb[i][j] == "O":
                    coordinates.append( (i,j))
        return coordinates
    
    #for x  in range(0,6,2):
    for x in range(0,4,2):
        state = states[x]
        mutate = fullstate.copy()
        coordinates = grabcoords(state)
        #print(mutate)
        while coordinates:
            i,j = coordinates.pop(-1)
            mutate[i] = mutate[i][:j:] + "."+ mutate[i][j+1::]
            for d in directions:    
                xcord = i + d[0]
                ycord = j + d[1]
                if xcord >= 0 and xcord <hieght and ycord >=0 and ycord <width:
                            
                    mutate[xcord] = mutate[xcord][:ycord:] + "."+ mutate[xcord][ycord+1::]
    
        states.append(mutate)
        states.append(fullstate)
    
    states = states[2::]
    states.pop(-1)
    print(states)
    if n == 1:
        return bomb
    if n == 3:
        
        return states[0]
    if n% 2 == 0:
        
        return states[1]
    
    term = math.ceil(n/4) - 1
    if 1 + (4 * term) == n:
        
        return states[2]
    else:
       
        return states[0]
