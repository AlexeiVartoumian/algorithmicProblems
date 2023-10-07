"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
"""

"""
theres a regex for this but hey lets make some functions :)
"""
def solution(inputString):
    
    
    if len(inputString) != 17:
        return False
    
    def isInteger(char):
        
        if char.isdigit():
            if int(char) >= 0 and int(char) <= 9:
                return True
        return False
    
    def ishex(char):
        
        return (ord(char) - 65 <= 5 and ord(char) -65 >=0)
    
    teststring = inputString.split("-")
    if len(teststring)!=6:
        return False
    for i in teststring:
        
        for j in i:
            if not isInteger(j) and not ishex(j):
                return False
    
    return True