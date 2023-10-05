"""
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false.
"""



def solution(bishop, pawn):
    
    directions = [(1,1),(1,-1),(-1,-1),(-1,1)]
    
    possmoves = set()
    
    
    startingposition = (ord(bishop[0])-97,int(bishop[1])-1)
    
    
    possmoves.add(startingposition)
    for d in directions:
        
        xcord = startingposition[0] + d[0]
        ycord = startingposition[1] + d[1]
        
        while xcord >=0 and xcord <8 and ycord >= 0 and ycord <8:
            possmoves.add((xcord,ycord))
            
            xcord+=d[0]
            ycord +=d[1]
    
    
    pawnCoords = (ord(pawn[0])-97,int(pawn[1])-1)
    
    return pawnCoords in possmoves
