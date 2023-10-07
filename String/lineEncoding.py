"""
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
for example, "aabbbc" is divided into ["aa", "bbb", "c"]
Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
for example, substring "bbb" is replaced by "3b"
Finally, all the new strings are concatenated together in the same order and a new string is returned.
"""
def solution(s):
    
    right =1
    output= ""
    count = 1
    curchar = s[0]
    while right < len(s):   
        if s[right] ==s[right -1]:
            count+=1
        else:   
            if count >1:
                output+= str(count)
                output+=curchar
            else:
                output+= curchar
            count = 1
            curchar= s[right]
        right+=1
    if count >1:
            output+= str(count)
            output+=curchar
    else:
            output+= curchar    
    return output