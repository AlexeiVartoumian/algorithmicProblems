"""
Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

Example:
S = "abaacdabd"
Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return 4.

Given a string s, convert it to the longest possible string t made up only of alternating characters. Return the length of string t. If no string  can be formed, return 0.

Returns.

int: the length of the longest valid string, or 0 if there are none.
constraints:

1<= length of s <= 1000
s[i] in the set of ascii[a-z]
"""

"""

In order to generate the largest possible string such that they are alternating a couple of things need to be observed. we can immediate ignore all instances of a characters in the string that appear consecutively and that we want the largest possible string such that we have the full number of each character.

my apporach works on the idea that given two letters if i can iterate through the string and as i go the next occuring letter is the alternate one and I can reach the end then its possible to construct a alternate string. for example in string
"ebedecb" with e and and b this is not possible since e is first then b then e but we see another e before another b occurs. building on this loop through the string using an auxilary character dictionary that keeps track of indexes of that character.
then use a comparison loop for on each character so long as: 

1.the difference between them is no greater than 1 i.e is possible to alterate
2.length of index of charA + length of indexes of charB is greater then previously seen.

if both above are true then apply modified merge procedure that asks the question
is the new list in ascending order. if so and we have reached the end of both char index lists then its possible to create an alternating string.

"""

from collections import defaultdict
def alternate(s):
    charindexes = defaultdict(list) # char as key list of indexes as value
    seen = set()
    chars = [] # used to uniquely compare two characters to see if they alternate
    prev = [] # use this to construct the ascending indexes
    total= 0 # will only apply modified merge procedure if length of char A + length of char B greater than total
    for i in range(len(s)):
        if s[i] not in seen:
            chars.append(s[i])
            seen.add(s[i])
        charindexes[s[i]].append(i)
    for i in range(len(chars)-1):
        for j in range(i+1, len(chars)):
            COUNTA = len(charindexes[chars[i]])
            COUNTB = len(charindexes[chars[j]])
            if abs(COUNTA - COUNTB) <=1 and (COUNTA + COUNTB > total):
                letterA = charindexes[chars[i]]
                letterB = charindexes[chars[j]]
                counta = 1
                countb= 0
                prev.append(charindexes[chars[i]][0])
                possible = True
                while possible and (counta < COUNTA and countb < COUNTB):
                    
                    if charindexes[chars[j]][countb] > prev[-1]:
                        prev.append(charindexes[chars[j]][countb])
                        countb+=1
                    else:
                        possible = False
                    if charindexes[chars[i]][counta] > prev[-1]:
                        prev.append(charindexes[chars[i]][counta])
                        counta+=1
                    else:
                        possible = False
                
                if abs(COUNTA - counta) >1 or abs(COUNTB - countb)>1:
                    possible = False
                if possible:
                    while possible and counta < COUNTA:
                        if charindexes[chars[i]][counta] > prev[-1]:
                            prev.append(charindexes[chars[i]][counta])
                            counta+=1
                        else:
                            possible = False
                        
                    while possible and countb < COUNTB:
                        if charindexes[chars[j]][countb] > prev[-1]:
                            prev.append(charindexes[chars[j]][countb])
                            countb+=1
                        else:
                            possible = False
                prev = []
                if possible:
                    total = max(total, COUNTA + COUNTB)
    return total