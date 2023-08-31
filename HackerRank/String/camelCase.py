"""
Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

Your task is to write a program that creates or splits Camel Case variable, method, and class names.

Input Format

Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
The operation will either be S (split) or C (combine)
M indicates method, C indicates class, and V indicates variable
In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.
Output Format

For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

def combine(token,string):
    temp = "".join([x.capitalize() for x in string.split(" ")])
    if token == "C":
        return temp
    elif token == "V":
        return temp[0].lower() + temp[1:]
    elif token == "M":
        temp = temp[0].lower() + temp[1:]
        return temp+"()"
        
def split(token,string):
    temp = " ".join(re.findall('[A-Z][^A-Z]*',string[0].capitalize() + string[1:])).lower()
    if "()" in temp:
        temp = temp[:-2]
    return temp

def main(txt):
    
    c,t,i = txt.split(";")
    if c == "C":
        print(combine(t,i))
    elif c == "S":
        print(split(t,i))

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        if 'Exit' == line:
            break
        main(line)