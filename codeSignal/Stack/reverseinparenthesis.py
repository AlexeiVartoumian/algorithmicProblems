
"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""

"""
stack procedure. whenever a close parenthesisis encountered then that is the innermost string to be reversed. this also means whenever an open parenthesis is encountered then the current output is to be stored. since all the brackets are well formed it doesnt matter if it is nested. whenever a close bracket is encountered reverse what ever the current output is which will be the innermost string at that point.
"""

def solution(inputString):
    
    
    output = ""
    stack = []
    for char in inputString:
        if char == "(":
            stack.append(output)
            output = ""
        elif char == ")":
            inner = output[::-1]
            output = stack.pop() + inner
        else:
            output += char
    return output