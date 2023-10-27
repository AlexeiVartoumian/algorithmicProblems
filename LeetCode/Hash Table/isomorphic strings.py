"""
Given two strings `s` and `t`, _determine if they are isomorphic_.

Two strings `s` and `t` are isomorphic if the characters in `s` can be
replaced to get `t`.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.
"""

#the below strings are not isomorphic
a="bbbaaaba"
b = "aaabbbba"
#the below strings are isomprohic
a1= "egg"
a2= "add"
"""
to determine if a string is isomorphic the order of the characters and the number of times a specific charavter occurs munst be held intact for both strings. for example with the strings egg and add the letters "e" and "a" respectively can be replaced with each other as they appear the same amount of times. the same is true for "gg" and "dd". as such the efficient solution directly below  maps the letter at each index to each other. if it has never occured before then map them together.if they have occured together then check if at the current iteration they still have the same corresponding values. this handles if they appear in the same order. After that its simply a case of checking for the length of values is equal to the length of the keys meaning handling the instance where the count of each respecitive character is the same in both strings.
IN OTHER WORDS ITS IMPORTANT THAT BOTH STRINGS MAP TO EACH OTHER    
EG FOO AND BAR we can see that the second o of foo maps to a diiferent character but what about bar to foo ? well b maps to f , a maps to o and r maps to o, we have to check both ways that they map to each character maps to the same character. this is what the last line below checks for that all unique characters do indeed map to the same character on both strings.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return len(set(d.values())) == len(set(d.keys()))
"""
my solution below does the same but not as effieciently I have a boolean array of length s that keeps track of the order of the occurences of characters. if the current element and the one ahead of it are the same and this is the case with the other string then the respective orders are the same and if not then they are not isomorphic. the dictionary handles the number of times each respective character occurs. then its a case of looping through the strings again checking that the count of each respective character is the same at the given position.
"""    


def isisormorphic(s,t):
        if len(s) != len(t):
            return False
        
        dicts = {}

        dictt= {}
        tableofjustice=[False] * len(s) 
        for i in range(len(s)-1):
            
            if s[i] != s[i+1] and t[i] != t[i+1]:
                tableofjustice[i] = True
            elif s[i] == s[i+1] and t[i] == t[i+1]:
                tableofjustice[i] = True
            else:
                return False
            if ord(s[i]) not in dicts:
                dicts[ord(s[i])] =1
            else:
                dicts[ord(s[i])]+=1

            if ord(t[i]) not in dictt:
                dictt[ord(t[i])]=1
            else:
                dictt[ord(t[i])]+=1
        
        if ord(s[-1]) not in dicts:
                dicts[ord(s[-1])] =1
        else:
                dicts[ord(s[-1])]+=1

        if ord(t[-1]) not in dictt:
                dictt[ord(t[-1])]=1
        else:
                dictt[ord(t[-1])]+=1
        for i in range(len(s)):
            if dicts[ord(s[i])] != dictt[ord(t[i])]:
                return False
        return True
isisormorphic(a,b)