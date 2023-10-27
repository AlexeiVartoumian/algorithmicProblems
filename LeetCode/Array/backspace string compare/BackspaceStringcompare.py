"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""
"""
use stack approach and merge procedure popping whenever a hash is encountered.
"""
def backspaceCompare(s, t):

        stacka= []
        stackb = []
        i = 0
        j = 0
        while i != len(s)-1 and j !=len(t):
            print(s[i],t[i])
            if s[i] == "#":
                if stacka:
                    stacka.pop()
                    
            else:
                    stacka.append(s[i])
                
            if t[j] == "#":
                if stackb:
                    stackb.pop()
                    
            else:
                    stackb.append(t[i])
            
            i+=1
            j+=1
        while i < len(s):
            
            if s[i] == "#":
                if stacka:
                    stacka.pop()
                    
            else:
                stacka.append(s[i])
            i+=1
        while j < len(t):
            
            if t[j] == "#":
                if stackb:
                    stackb.pop()
                    
            else:
                    stackb.append(t[j])
            j+=1
        return stacka == stackb
