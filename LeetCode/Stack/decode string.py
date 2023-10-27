"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
"""
the premise is as follows , we know that for every opened bracket "["
all consequent characters will be multiplied by the int string. therefore we use a stack like procedure and say the following.
whenever we encounter a "]" then we need to multiply whatever was inside those brackets (which is of course a string) which we call current string multiply it by the required int string and add that concatanated string to the previous string. 
in order to do this whenever we encounter a "[" we store the current string whatever it is with the number forcemultiplier as a tuple( this current string will be previous string as ntoed above) and reinitilaise the current number and current string.this will handle all instances of characters appearing between brackets. finally if we have a condition where its current string element is niether a "[" or "]" then we add that element to the current string.finally to handle string digits like "13" we first set current number to zero. then we grab the integer value and add it to whatever current number is multiplied by 10. example currentnumber is 0 and first element in string is 1. then multiply 0 * 10 and add 1 to represent 1. next value is 3. then multiply 1 by 10 to get 10 and and the integer value . in this fashion we get 13 or any number longer than length 1.
"""

def decodestring(s):

      stack = []
      currentstring = ""
      currentnumber = 0
      for c in s:

          if c.isdigit():
              currentnumber = currentnumber * 10 + int(c)
          elif c == "[":

              stack.append((currentstring,currentnumber))
              currentnumber = 0
              currentstring = ""

          elif c == "]":
              previousstring , multiplier = stack.pop()
              currentstring = previousstring +(currentstring * multiplier)
          else:
            currentstring += c

      return currentstring  
        

class Solution:
  def decodeString(self, s: str) -> str:
    ans = ''

    while self.i < len(s) and s[self.i] != ']':
      if s[self.i].isdigit():
        k = 0
        while self.i < len(s) and s[self.i].isdigit():
          k = k * 10 + int(s[self.i])
          self.i += 1
        self.i += 1  # '['
        decodedString = self.decodeString(s)
        self.i += 1  # ']'
        ans += k * decodedString
      else:
        ans += s[self.i]
        self.i += 1

    return ans

  i = 0