"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string inputString

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 50.

[output] boolean

true if the characters of the inputString can be rearranged to form a palindrome, false otherwise.
"""
 #check if input is odd then one letter can have odd number else all letters must be even

def solution(inputString):
    
   
    
    
    length = len(inputString)
    
    counts = {}
    
    for i in  inputString:
        
        counts[i] = 1 + counts.get(i,0)
    
    
    odds = False
    if length % 2 == 0:
        
        for i,x in counts.items():
            if x % 2 ==1:
                return False
    
    else:
        for i,x in counts.items():
            if x % 2 == 1 and not odds:
                odds = True
            elif x % 2 == 1 and odds:
                return False
    
    return True