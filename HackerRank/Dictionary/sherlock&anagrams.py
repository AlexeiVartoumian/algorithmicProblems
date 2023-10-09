"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example

The list of all anagrammatic pairs is  at positions  respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below.

sherlockAndAnagrams has the following parameter(s):

string s: a string
Returns

int: the number of unordered anagrammatic pairs of substrings in 
Input Format

The first line contains an integer , the number of queries.
Each of the next  lines contains a string  to analyze.

Constraints



 contains only lowercase letters in the range ascii[a-z].

Sample Input 0

2
abba
abcd
Sample Output 0

4
0
Explanation 0

The list of all anagrammatic pairs is  and  at positions  and  respectively.

No anagrammatic pairs exist in the second query as no character repeats.

Sample Input 1

2
ifailuhkqq
kkkk
Sample Output 1

3
10
Explanation 1

For the first query, we have anagram pairs  and  at positions  and  respectively.

For the second query:
There are 6 anagrams of the form  at positions  and .
There are 3 anagrams of the form  at positions  and .
There is 1 anagram of the form  at position .

Sample Input 2

1
cdcd
Sample Output 2

5
Explanation 2

There are two anagrammatic pairs of length :  and .
There are three anagrammatic pairs of length :  at positions  respectively.
"""
def sherlockAndAnagrams(s):
    # Write your code here
    
    """
    so im going brute force approach where I will generate every possible
    substring and compare it with every other subastring
    such that is poosible to make so long as it repsects the bounds
    of the string. as such for every such substring I make the comparison
    and iask the question does the freqeuncy of my current window
    mathc the frequency of the current string? if so then increment count
    i have an anagram. use a sliding window to decrement right and left
    pointers decreasing and increasing respective achar icounts
    """
    count = 0
    for i in range(len(s)):
        
        for j in range(i ,len(s)): # this nested lop is genreating my current window
            currentwindowlength = (j - i) + 1
            currentwindow = {}
            if i + currentwindowlength <=len(s):
                for z in range(i , i + currentwindowlength):
                    currentwindow[s[z]] = 1 + currentwindow.get(s[z],0)
                # i have now made my current window
                #from here the goal is to compare all i + 1 substrings
                #therefore check if in bounds
                if i+1 + currentwindowlength <= len(s):
                    tempwindow = {}
                    right = i+1
                    for z in range(i+1,(i+1 +currentwindowlength)):
                        tempwindow[s[z]] = 1 + tempwindow.get(s[z],0)
                        right = z
                    #its at this point i shift the window
                    #incrementeing and derementing accoriding to pointers
                    left = i+1
                    for x in range(right+1, len(s)):
                        if tempwindow == currentwindow:
                            count+=1
                        tempwindow[s[left]]-=1
                        if tempwindow[s[left]] == 0:
                            del(tempwindow[s[left]])
                        tempwindow[s[x]] = 1 + tempwindow.get(s[x],0)
                        left+=1
                    if tempwindow == currentwindow:
                        count+=1
            else:
                continue
            
                    
            
    return count