"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

"""
bim bam bop
"""

class Solution:
    def reverseWords(self, s: str) -> str:

        arr = s.split(" ")


        output = ""
        for i in range(len(arr)-1,-1,-1):
            if arr[i] == "":
                continue
            else:
                output+= arr[i]
                output+=" "
        
        return output[0:-1]

def reverseWords(self, s: str) -> str:
        a = s.split()
        
        a = a[::-1]

        return " ".join(a)