





"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.

Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

Example.


aab shortens to b in one operation: remove the adjacent a characters.


Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

Function Description

Complete the superReducedString function in the editor below.

superReducedString has the following parameter(s):

string s: a string to reduce
Returns

string: the reduced string or Empty String
Input Format

A single string, .

Constraints

Sample Input 0

aaabccddd
Sample Output 0

abd
Explanation 0

Perform the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd
Sample Input 1

aa
Sample Output 1

Empty String
Explanation 1

aa → Empty String
Sample Input 2

baab
Sample Output 2

Empty String
Explanation 2

baab → bb → Empty String
"""
"""
the way I approached this was to keep slicing whenever a two adjacent chars are identical. if its possible to iterate throughout the entire string then at no point are two chars identical.
"""

def superReducedString(s):
    # Write your code here
    output = s
    flag = True
    while flag:
        
        found = False
        for i in range(len(output)-1):
            if output[i] == output[i+1]:
                output = output[:i]+ output[i+2::]
                found = True
                break      
        if not found:
            flag = False
    if output == "":
        return "Empty String"
    return output