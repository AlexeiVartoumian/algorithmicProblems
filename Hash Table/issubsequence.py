
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

""" the approach here is to use j to as a tracker to see if we can traverse all the elements of s in order within the range of the greater length of the string t . if at any point a character in s does has not appeared in t then we continue traversing through the t until that character occurs. after this the only thing to do is to check if k is equal to the length of s or in toher words if all the letters of s are in fact a subsequence of t."""

def issubsequence(s,t):
        j = 0
        if s == "":
            return True
        
        for i in range(len(t)):
           
            if j == len(s):
                return True
            if s[j] == t[i]:
                j+=1 

        print(j, len(s)-1,"hello")
        return j == len(s)