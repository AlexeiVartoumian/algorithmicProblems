"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1
Explanation

Test Case #01: We split  into two strings ='aaa' and ='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams.

Test Case #02: You have to replace 'a' with 'b', which will generate "bb".

Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another.

Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one.

Test Case #05:  and  are already anagrams of one another.

Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".
"""

"""
there are many ways to do this problem because the core of the problem is to count the number of differences between the two strings of half length of orginal string.
as such i have an object/ record for each string storing all the letters as keys and the frequency in which they occur in thier respective string as value.

once this has been computed calculate the absolute difference between the two dictionarys. the number of letters it takes to form both into anagrams of each other will be the sum of those differences divided by two.
"""

def anagram(s):
    # Write your code here
        if len(s) % 2 ==1:
            return -1
        
        s1= s[:len(s)//2:]
        s2 = s[len(s)//2::]
        
        s1obj = {}
        s2obj = {}
        letters = []
        for i in range(26):
            letter = chr(i+97)
            s1obj[letter] = 0
            s2obj[letter] = 0            
            letters.append(letter)
        
        for i in range(len(s1)):
            s1obj[s1[i]] += 1 
            s2obj[s2[i]]+=1
        operations = 0
        
        for i in letters:
            
            operations += abs(s1obj[i] - s2obj[i])
        return operations //2