
"""Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.



For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.
"""

"""
since chess board cell colours alternate according to letter and number find the numerical representation of these
"""

def solution(cell1, cell2):
    
    
    """
    if letter is even then for each odd number it will have a light square. opppsoite is true for odd colours. alternate between each one.
    """
    
    colours = ["WHITE","BLACK"]
    var1 = ""
    var2 = ""
    
    ord(cell1[0])
    ord(cell2[0])
    
    def determine(letter, number):
        
        if letter %2 == 1:
            if number %2 == 0:
                return colours[0]
            return colours[1]
        else:
            if number %2 == 0:
                return colours[1]
            return colours[0]
    
    var1 = determine(ord(cell1[0]), int(cell1[1]))
    var2 = determine(ord(cell2[0]),int(cell2[1]))
    return var1 == var2