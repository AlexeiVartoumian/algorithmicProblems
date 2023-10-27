"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"""

"""
the first obseervation to make is that a substring to be a substring has to be contiguous. therefore the idea is pretty straightforward after this
have a vowels count and a window starting at 0 to length k of intial string. after that just make comparisons at every step and see if vowel count is larger than previous
"""
def maxVowels(self, s: str, k: int) -> int:

        window= {}

        string = "aeiou"
        vowels = set()
        curcount = 0
        maxcount =0
        for i in string:
            vowels.add(i)
        
        for i in range(k):
            window[s[i]] = 1 + window.get(s[i],0)
            if s[i]in vowels:
                curcount +=1
                maxcount = curcount
        
        left= 0
        right = k
        for i in range(right, len(s)):
            
            window[s[left]]-=1
            if window[s[left]] == 0:
                del(window[s[left]])
            if s[left] in vowels:
                curcount-=1
            left+=1
            window[s[i]] = 1 + window.get(s[i],0)
            if s[i] in vowels:
                curcount+=1
            maxcount = max(maxcount,curcount)
        return maxcount
def maxVowels(self, s: str, k: int) -> int:
        vowels = 0
        
        
        valid = set(['a', 'e', 'i', 'o', 'u'])

        for i in range(k): 
            
            if s[i] in valid: 
                vowels += 1 
        ans = vowels 

        for i in range(k,len(s)):
            
            if s[i] in valid: 
                vowels += 1
            
            if s[i-k] in valid:
                vowels -=1
            ans = max(ans,vowels)
            
        return ans

