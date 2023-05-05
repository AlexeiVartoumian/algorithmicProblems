""" stack question"""
s = "{[]}"

def validparenthesis(s, stack=[]):
    
    if s == "":
        return len(stack) == 0
    if s[0] == "]" or s[0] == "}" or s[0] == ")":
        
        if stack:
            cur = stack.pop()
            if s[0] != cur:
                return False
        elif not stack and s:
            return False
        
        return validparenthesis(s[1:],stack)
    
    else:
        if s[0] == "(":
            stack.append(")")
        elif s[0] == "{":
            stack.append("}")
        elif s[0] == "[": 
            stack.append("]")
        return validparenthesis(s[1:],stack)
print(validparenthesis(s) )
def valid( s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif not stack or stack.pop() != c:
                return False
        return not stack