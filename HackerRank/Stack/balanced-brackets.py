"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

Function Description

Complete the function isBalanced in the editor below.

isBalanced has the following parameter(s):

string s: a string of brackets
Returns

string: either YES or NO
"""

"""
this is a stack question. considering the properties of well-formed brackets specifically in a sequence like the one given we know as soon as a closing bracket occurs then we have reached the inner most bracket. the solution is to append all "open" brackets to a stack and ask a series of questions , if close appears and stack is empty it is not balanced. if they last appended item does not match then they do not match. otherwise pop the last open bracket from the stack. if an open brack is in the string then append it to stack .finally check if there are still items in open brackets if there are none reutrn yes they are balnaced brackets. in all other cases return No.
"""

def isBalanced(s):
    # Write your code here
    openbrackets = {"{","(","["}
    close = {"}",")","]"}
    relation = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }
    openstack = []
    for i in range(len(s)):
        if s[i] in close:
            if not openstack:
                return "NO"
            elif relation[s[i]] != openstack[-1]:
                return "NO"
            else:
                openstack.pop(-1)
        elif s[i] in openbrackets: 
            openstack.append(s[i])
    
    if len(openstack) >0: 
        return "NO"
    return "YES"