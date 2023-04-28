"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""
"""
using a hashmap store a string of length 10 as the key. start iterating from position 10 of string.  use sliding window to compare at each iteration if current string has been seen before in dictionary. if so have anohter dicitonary to check if there if more than one instance of it to avoid duplicates.
"""

def findRepeatedDnaSequences(s):

        
        theobject = {}
        alreadyin = {}

        currentstring = s[0:10]

        theobject[currentstring] =1

        left =10
        results = []
        for i in range(left,len(s)):
            
            currentstring = currentstring[1:] + s[i]
            if currentstring in theobject:
                if currentstring not in alreadyin:
                    results.append(currentstring)
                    alreadyin[currentstring] = 1
            else:
                theobject[currentstring] = 1
        
        return results