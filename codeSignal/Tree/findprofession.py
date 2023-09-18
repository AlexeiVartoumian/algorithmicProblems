"""
Consider a special family of Engineers and Doctors. This family has the following rules:

Everybody has two children.
The first child of an Engineer is an Engineer and the second child is a Doctor.
The first child of a Doctor is a Doctor and the second child is an Engineer.
All generations of Doctors and Engineers start with an Engineer.
We can represent the situation using this diagram:

                E
           /         \
          E           D
        /   \        /  \
       E     D      D    E
      / \   / \    / \   / \
     E   D D   E  D   E E   D
Given the level and position of a person in the ancestor tree above, find the profession of the person.
Note: in this tree first child is considered as left child, second - as right.

Example

For level = 3 and pos = 3, the output should be
solution(level, pos) = "Doctor".
"""

"""
the first thing to observe is this tree will always follow a set pattern
"EDDE" followed by "DEED" and that this is a perfectly balanced tree.
second if one was to think of a given position and level as the index of the contiguous combination  of the above array, the goal is then to find out what that value will be. this is known as the thue morse sequence where if we instead treat the "EDDE" and "DEED" as boolean values i.e "0110" and "1001" we can then say they are the complement of each other. the idea then is to find the parity of the given position reducing the number with bitwise AND. after than just check if count is odd or even.
"""

def solution(level, pos):
    
    
    
    
    def countsequence(bit):
        
        count = 0
        while bit >0:
            
            bit &= bit-1
            count+=1
        
        return count 
    
    if countsequence(pos-1) % 2 == 0:
        return "Engineer"
    return "Doctor"