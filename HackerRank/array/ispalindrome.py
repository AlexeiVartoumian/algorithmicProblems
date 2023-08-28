"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.

Example

Either remove 'b' at index  or 'c' at index .

Function Description

Complete the palindromeIndex function in the editor below.

palindromeIndex has the following parameter(s):

string s: a string to analyze
Returns

int: the index of the character to remove or 
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a query string .

Constraints

All characters are in the range ascii[a-z].
Sample Input

STDIN   Function
-----   --------
3       q = 3
aaab    s = 'aaab' (first query)
baa     s = 'baa'  (second query)
aaa     s = 'aaa'  (third query)
Sample Output

3
0
-1
"""

"""
my initial solution works but is innefficient becaus it removes every char at every index and computes the string and  its reverse whereas a more efficient approach is to basucally do the same only when the i-th index and its corresponding idnex value len(s)-i -1 do not equal to each other and then take the char out and make the computation then. 
"""


def palindromeindex(s):

    def ispalindrome(s):
        if s == s[::-1]:
            return True
    
    if ispalindrome(s):
        return -1
    
    for i in range(len(s)):
        
        if s[i] != s[len(s)-1 -i]: # if corresponidng indexes dont match

            news = s[:i:]+ s[i+1::]
            news2 = s[:len(s)-i-1:] + s[len(s)-i]
            if ispalindrome(news):
                return i
            elif ispalindrome(news2):
                return len(s) -i - 1
    return -1


def palindromeIndex(s):
    # Write your code here
    if len(s) % 2 == 0:
        middle = int(len(s)/2)
        if s[:middle:] == s[-1:middle-1:-1]:
            return -1
        else:
            for i in range(len(s)):
                combo= s[:i:] +s[i+1::]
                middle = int(len(combo)/2)
                if combo[:middle:] == combo[-1:middle:-1]:
                    return i
            return -1 
    else:
        middle = int(len(s)/2)
        if s[:middle:] == s[-1:middle:-1]:
            return -1
        else:
            for i in range(len(s)):
                combo= s[:i:] +s[i+1::]
                middle = int(len(combo)/2)
                if combo[:middle:] == combo[-1:middle-1:-1]:
                    return i
            return -1