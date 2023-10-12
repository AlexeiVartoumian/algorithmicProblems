"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example

This is a valid string because frequencies are .


This is a valid string because we can remove one  and have  of each character in the remaining string.


This string is not valid as we can only remove  occurrence of . That leaves character frequencies of .

Function Description

Complete the isValid function in the editor below.

isValid has the following parameter(s):

string s: a string
Returns

string: either YES or NO
Input Format

A single string .

Constraints

Each character 
Sample Input 0

aabbcd
"""

"""
the general approach I took was to count the number of times every chracter appears in the string and then create an object
counting all the frequencies that are greater than zero. after this there are numerous edge cases to consider
case1 freq object is length 1 return true or greater than 2 return false
edge cases need to be considered when the frequency object is of length 2 for example
the subtraction of the greatest element or smallest element is eqaul to zro then return true
the absolute difereence is greater than 1 but the smallest occuring frequency is not 1 return false eg: a:2000 , b :2 => false
but a:2000 , b:1 => true
"""
def isValid(s):
    # Write your code here
    letters = [0] * 26
    for i in s:
        
        letters[ord(i)-97] +=1    
    freqs = {}
    largest = max(letters)
    smallest = max(letters)
    for i in letters:
        if i != 0:
            freqs[i] = 1 + freqs.get(i,0)
            smallest = min(largest,i)
    if len(freqs) == 1:
        return "YES"
    if len(freqs) >2:
        return "NO"
    if abs(largest-smallest) > 1 and freqs[smallest] != 1:
        return "NO"
    if freqs[largest]-1 == 0 or freqs[smallest]-1 == 0:
        return "YES"
    
    return "NO"
