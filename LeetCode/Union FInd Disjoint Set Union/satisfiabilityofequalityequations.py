
"""
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
"""





"""
since we are cheking onyu for two operations the approach is to 
first loop through all equations that are equal to each other, with 
the goal being to assign a "root" value.to represent this we use an object
with letters a- z as key and its own letter as init value which could be updated.
this will be later needed to 
traverse for eg a test case where a==b b==c c == d .we will use a find
function that will recursively traverse to find a root value where the 
base case will be something like a == a. whenever we have find a value
that is not the same then we recursively find the root value
and update it after assigning all
values then go through the equations that are not equal to each other.
and "find" the respective root values of each equation. if they are
equal to each other return False. otherwise if loop is successful return 
true
"""
b =["e==d","e==a","f!=d","b!=c","a==b"]

def equa(equations):
    theobject = {chr(num): chr(num) for num in range(ord("a"),ord("z")+1)}
    
    def find(value):
        if theobject[value]== value:
            return value
        theobject[value] =find(theobject[value]) #above means they are not equal so traverse
        return theobject[value]
    
    for equation1, operation,filler,equation2 in equations:
        if operation == "=":
            root1 =find(equation1)
            root2 = find(equation2)
            theobject[root1] = root2
    
    for equation1, operation,filler,equation2 in equations:
        if operation =="!":
            if find(equation1) == find(equation2):
                return False
    return True

equa(b)