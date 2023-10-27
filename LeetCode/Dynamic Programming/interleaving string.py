"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
"""
"""
My  first tried to work backwards from the str3 and moving to front position by using two pointers at str1 and str2. it was close but not quite as this is in fact a dp problem where you have to bubble up the boolean at each case where a decision can be made to either choose on char or the other. this requires a nested structure of length n * m .
"""

def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        records = [ [False ]* (len(s2)+1) for i in range(len(s1)+1)]

     
        records[len(s1)][len(s2)] = True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):

                if i < len(s1) and s1[i] == s3[i+j] and records[i+1][j]:
                    records[i][j] = True
                
                if j < len(s2) and s2[j] == s3[i+j] and records[i][j+1]:
                    records[i][j] = True
        
        return records[0][0]


"""
1st attempt
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        records = [0]* len(s3)
    
        i = len(s1)-1
        j = len(s2)-1
        k = len(s3)-1
        if len(s1) + len(s2) != len(s3):
            return False
        if records:
            while records[0] == 0:
        
                if  i >=0 and s1[i]== s3[k]:
                    while s1[i]== s3[k] and i >= 0:
                        records[k] = s1[i]
                        k-=1
                        i-=1
                elif j >=0 and s2[j] == s3[k] :
                    while s2[j] == s3[k] and j>=0:
                        records[k] = s2[j]
                        k-=1
                        j-=1
                else:
                    return False
        
        return True