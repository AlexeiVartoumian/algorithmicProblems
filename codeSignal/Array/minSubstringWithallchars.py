"""
You have two strings, s and t. The string t contains only unique elements. Find and return the minimum consecutive substring of s that contains all of the elements from t.

It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

Example

For s = "adobecodebanc" and t = "abc", the output should be
solution(s, t) = "banc".
"""

"""
sliding window problem. the test case is perfect as eit highlights how we should use the two pointers to slide. at the first pass the right pointer will keep moving until it hits "c"  because t = "abc" and first instance where all letters occur in s is "adobec". this instigtes another while loop where so long as the length og the target characeters is equal to the length of the dictionary containing all letters keep moving left. in the example adobec we encounter "a" which is in the set so remove it and the inner while loop will exit. left is now 1. the right pointer will move alone until the length is equal where the inner loop will keep asking the same two things. is current index right - left +1 less then smalles seen string? is yes string slice at those two points. other wise keep moving left until the length of the two are no longer the same.
"""
s = "adobecodebanc" 
t = "abc"
def solution(s,t):

    chars = set(t)

    target = {}

    length = float("inf")
    string = ""

    left= 0
    right = 0

    while right < len(s):

        if s[right] in chars:

            target[s[right]] = 1 + target.get(s[right],0)

        while len(target) == len(chars):

            if right - left+ 1 < length:
                length = right - left +1
                string = s[left:right+1:]

            if s[left] in target:
                target[s[left]]-=1
                if target[s[left]] == 0:
                    del(target[s[left]])
            left+=1
        right +=1
    return string
