"""
An input string controls the movement of a robot, 
"F" means move 1 step forward, "L" means turn 90 degrees 
to the left and "R" means turn 90 degrees to the right. 
E.g. "FLF" moves the robot one step forward, 
then turns it left by 90 degrees, then moves the robot one step forward.
Write a function that returns the minimum 
number of commands that the robot needs to 
return to it's starting point after following all the input 
commands. You should return any characters that are not capital 
F, L, or R. HINT: You may wish to track the robots position using 
(X,Y) coordinates, assuming it starts at (0,0).
Example:
. "RF" returns 3 (robot must turn twice and move forward one step 
(e.g. "RRF")
. "LFRFRFR" returns 1 (robot must step forward to return )
. "FxLxLxFx" returns 0 (robot is already back at starting point )
"""
"""
I had this in an interview and I failed to consider different edge cases so here I was very pedantic 
"""
#inputs = "LFRFRFR"
#inputs= "LFFLFFL"
#inputs = "RF"
inputs = "FFFFFRFFFFFR"


def returntoorigin(inputs):
    coords = [0,0]
    face = "U"
    directions = {"D":(0,-1),
                  "U":(0,1),
                  "R":(1,0),
                  "L":(-1,0)
                  }
    def determine(current,nextinstruction):
        if current == "U": return nextinstruction
        if current == "D": # this got me in th interview when facing down if you take a left its the opposite of taking a left if your facing up.
            #like looking in a mirror.
            if nextinstruction == "R": return "L"
            return "R"
        if current == nextinstruction: return "D"
        return "U"
    def operationcost(curdirection,neededdirection):
        if curdirection == neededdirection:
            return  0
        elif curdirection == "U" or curdirection == "D":
            return 1
        elif curdirection == "L" and neededdirection == "U" or curdirection == "R" and neededdirection == "U":
            return 1
        elif curdirection == "L" and neededdirection == "D" or curdirection == "R" and neededdirection == "D":
            return 1
        else:
            return 2
    def findx(xcord): #ties in with the directions dicitonary  
        if xcord >0:
           return "L"
        else:
            return "R"
    def findy(ycord):
        if ycord >0:
            return "D"
        else:
            return "U"
    for i in range(len(inputs)):
        if inputs[i] in directions:
            face = determine(face,inputs[i])
           
        elif inputs[i] == "F":
            xcord = directions[face][0]
            ycord = directions[face][1]
            coords[0] += xcord
            coords[1] += ycord
            #print("Coords", coords)

    res = 0
    #print(coords[0],coords[1],face)
   
    if coords[0] != 0 and coords[1] != 0: # 
        if operationcost(face,findx(coords[0])) < operationcost(face,findy(coords[0])): # handle the case where cur direction is optimal for one cordinate
            #first x then y
            res+= operationcost(face,findx(coords[0]))
            face  = findx(coords[0])
            res+= abs(coords[0])

            res+= operationcost(face,findy(coords[1]))
            face = findy(coords[1])
            res+= abs(coords[1])
        else:
            res+= operationcost(face,findy(coords[1]))
            face = findy(coords[1])
            res+= abs(coords[1])

            res+= operationcost(face,findx(coords[0]))
            face  = findx(coords[0])
            res+= abs(coords[0])
    else:
        if coords[0] == 0:
            res+= operationcost(face,findy(coords[1]))
            face = findy(coords[1])
            res+= abs(coords[1])
        else:
            res+= operationcost(face,findx(coords[0]))
            face  = findx(coords[0])
            res+= abs(coords[0])
    return res


print(returntoorigin(inputs))

