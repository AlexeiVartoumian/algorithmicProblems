
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
Explanation

Query 1: "aaab"
Removing 'b' at index  results in a palindrome, so return .

Query 2: "baa"
Removing 'b' at index  results in a palindrome, so return .

Query 3: "aaa"
This string is already a palindrome, so return . Removing any one of the characters would result in a palindrome, but this test comes first.

Note: The custom checker logic for this challenge is available here.
"""


"""
since the task is to consider all instances where removing a SINGLE letter to turn the entire string into a palindrome all that has to be done is to find the first instance where two letters do not match on 
either end of the spectrum. if by taking out one of these letters a plaindrome is not formed and furthtermore the same is true for the other side then we know that at LEAST two letters will have to be removed in order to generate a palindrome. other wise return either the low or high index. so this is actually a two pointer problem but it works in the fashion of a binary search where istead os findingt the middle point
the left and right pointer move in twords each other one step at a time.
"""




def palindromeIndex(s):
    # Write your code here

    def isPalindrome(s,low,high):
        while low <high:
            if s[low]!= s[high]:
                return False
            low+=1
            high-=1
        return True
    
    low = 0
    high =len(s)-1
    
    while low < high:
        if s[low] == s[high]:
            low+=1
            high-=1
        else:
            if isPalindrome(s,low+1,high):
                return low
            
            elif isPalindrome(s,low,high-1):
                return high
            return -1
    return -1