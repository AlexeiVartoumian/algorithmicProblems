"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

"""
a couple of observations to make here is thast the last item in the stack will alaways be an operation and that given an operation it will always require two operands one on each side of it. as such for reverse polish notation all that has to be done is to append any digit wether it is positive or negative and to keep doing so until an operation is encountered. once so pop the last two numbers keeping in mind that the first pop will be the number on the righthandside of the expression and the second pop will be the number on the lefthandside of the expression. perform the calculation and append this number to the stack. return int(stack[0])
"""

def reversepolish(tokens):

    stack= []
    #all vals in tokens are strings
    for i in tokens:
        #account for string versions of positive and negative numbers
        if i.isdigit() or len(i) >= 2 and i[0] == "-": 
            stack.append(i)
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if i == "+":
                val = int(num1)+ int(num2)
                stack.append(val)
            if i == "-":
                val = int(num1)+ int(num2)
                stack.append(val)
            
            if i == "*":
                val = int(num1)+ int(num2)
                stack.append(val)
            
            if i == "/":
                val = int(num1)+ int(num2)
                stack.append(val)
    return int(stack[0])





def evalRPN(self, tokens: List[str]) -> int:

    
        stack = []

        for i in tokens:
           
            if i.isdigit() or (len(i) >=  2 and i[0] == "-"):
                stack.append(i)
                
            else:
                
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    val = int(num1) + int(num2)
                    stack.append(val)
                if i == "/":
                    val = int(num1) / int(num2)
                    
                    stack.append(val)
                if i == "*":
                    val = int(num1) * int(num2)
                    
                    stack.append(val)
                if i == "-":
                    val = int(num1) - int(num2)
                    stack.append(val)
        
        return int(stack[0])