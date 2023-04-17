"""
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""
"""
The idea is to start wiht a two pointers for left and right. a 
single letter is by definition a palindrome. after that check on each side of
that letter if they are the same. this works for odd. for even set the 
right pointer to one ahead of left instead of at same point. at every step check the current position of the right - left + 1  that is the current subtring length ( +1 to account for the index) is longer than the current string length 
"""

"""
        the idea is to use a middle out approach on every letter as you loop through itusing a left and right
        pointer to iterate outwards a middle out :) . so long as each element is equal to each other you have a valifd
        anagram. however the thing to keep in mind here is that we have od and even anagrams. therefore
        to account for this two while loops need to be executed, one where both pointers start at a given
        element and another where the right pointer startsone ahead of left pointer for even anagram.
        whenever the length of right - left is greater or equal than length of current output update the output
        with string slice
"""

def longestPalindrome(self, s: str) -> str:
        output = ""
        for i in range(len(s)):
            left,right = i,i
            #middle out
            while right < len(s) and left >= 0 and s[left] == s[right]:
                if right - left >= len(output):
                    output = s[left:right+1]
                left-=1
                right+=1
            #handle even anagrams 
            left = i
            right = i+1
            while right < len(s) and left >= 0 and s[left] == s[right]:
                if right - left >=len(output):
                    output = s[left:right+1]
                left-=1
                right+=1
        
        if not output :
            return s[0]
        return output

def longestpalindrome(s):

    resultlength = 0
    output = ""

    for i in range(len(s)):

        left,right = i,i

        while left >= 0 and right < len(s)-1 and s[right] == s[left]:
            
            if right - left+1 > resultlength:
                resultlength = right - left +1 
                output = s[left:right+1]
            
            right+=1
            left -=1
        
        left,right = i,i+1
        while left >=0 and right < len(s)-1 and s[right] == s[left]:
            if right - left+1 > resultlength:
                resultlength = right - left +1
                output = s[left:right+1]
    
    return output










class Solution:
    def longestPalindrome(self, s: str) -> str:

        out = ""

        resultlength = 0

        for i in range(len(s)):

            left,right = i,i

            while left >=0 and right <len(s) and s[left] == s[right]:

                if right - left+1 >= resultlength:
                    resultlength = right - left+1
                    out = s[left:right+1]
                
                right+=1
                left -=1
            
            left ,right = i, i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left+1 >= resultlength:
                    resultlength = right - left+1
                    out = s[left:right+1]
                right+=1
                left-=1
        
        
        return out