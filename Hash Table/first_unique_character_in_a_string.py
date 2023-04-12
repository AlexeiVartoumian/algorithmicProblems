"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""
"""
the danger of this problem is that we only want the first occurence of a unique cahracter- this should require to loop thorugh the entire list and keep track of the number of occurences a character occurs. where i went wrong was to delete non-unique values as I traversed the array which meant I had to have another array to store non-unique values. it was also a case of looping through the values of the dictionary where the indexes are stored as values and then seeing if that value is in the non 0unique array.
A much better solution would be  the one directly below essentially does the same thing but avoids the problem i encountered by storing all letters in a set and deleting and adding elements only if they have been seen in the set.
"""
def firstUniqChar(s):
        chars_seen = set()
        char_idx_dict = {}

        for idx, char in enumerate(s):
            if char not in chars_seen:
                chars_seen.add(char)
                char_idx_dict[char] = idx
            else:
                if char in char_idx_dict:
                    del char_idx_dict[char]
        
        if len(char_idx_dict) > 0:
            return sorted(char_idx_dict.values())[0]
        else:
            return -1
def firstUniqChar(self, s: str) -> int:

        unique = set()
        theobject={}

        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
                theobject[s[i]] = i
            else:
                if s[i] in theobject:
                    del(theobject[s[i]])
                    
        
        if len(theobject) > 0 :
            cursmall = len(s)
            for i in theobject.values():
                if i < cursmall:
                    cursmall = i
            
            return cursmall
        else:
            return -1


def firstUniqChar(s):

        theobject= {}
        badobject=[]
        curmin = -1
        for i in range(len(s)):
            if s[i] in theobject:
                badobject.append(s[i])
                del theobject[s[i]]
                if theobject != {}:
                    curmin = min(theobject.values())
                else:
                    curmin = -1
            else:
                if curmin == -1:
                    curmin = i
                    theobject[s[i]] = i
                else:
                    
                    theobject[s[i]] = i
        print(theobject,curmin,badobject)
        for i in theobject.values():
            if s[i] not in badobject:
                if s[curmin] in badobject:
                    curmin = i
            elif i == curmin:
                curmin = -1
        
        if curmin != -1:
            return curmin
        return -1
        