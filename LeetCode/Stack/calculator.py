""""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

"- (3 + (4 + 5))"
"1-(     -2)"
"2147483647"
"""


"""
    we approach this bu linearly going through the string.
    we keep track of the following: open/close parentheses
    if cur char is a digit and if the operator is plus or minus.
    because of the parenthesis the order of operations is dependant on 
    the number of of open-to close parenthesis. as such
    we have a variable that keeps track of the "state" that is positive
    or negative and stored in stack when open parenthesis occurs.
    . when close parenthesis occurs then pop it off.
    then whenever the + or - operator 
    occurs this is applied to result  that is result += sign * number and then set number to zero. 
    we update this "state" in a stack making sure to switch it
    whenever a minus occurs since minus* minus will make a positive.
    finally reurn the result multiplied by sign + number
"""

class Solution:
    def calculate(self, s: str) -> int:

       
        number =0
        state =1
        stack = [state]
        result = 0

        for i in s:

            if i.isdigit():
               number = number*10 + int(i)
            elif i == "(":
                stack.append(state)
            elif i == ")":
                stack.pop()
            elif i == "+" or i =="-":
                result += number * state
                state = (1  if i == "+" else -1) * stack[-1]
                number = 0
        
        return result + state * number
