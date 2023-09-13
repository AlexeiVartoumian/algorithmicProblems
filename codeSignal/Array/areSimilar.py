"""
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""

"""
initial approach was to keep an object where I would keep mismatched values as key with thier respective number in opposite array as 
    im thinking to map an integer to an integer in respective arrays whenver
    they are different. if it happens again check if the other one is the "complemnt" of the item. if yes then that one swap will achiecve a similar array. if it does not it means we have three different elements and therefore
    it will be impossible to make the arrays similar with only one swap. so long as length of this object is less than or equal to two and the count of differing occuring elements is less than or equal to two its all good. however I was missing an edge case.

    as such the second appraoch is of a similar idea have a count that keeps track of whenver a mismatch occurs.
    when it does increment it and append respective numbers to temp arrays. the idea here is at the end of the loop if the number of mismatches is greater than 2 or if the reverse of one of the arrays does not equal to the other array return false.
    eg [1,2,3]  , 
       [2,1,3]
    tempa = [1,2] at end of iteation
    tmpb = [2,1] at end of iteration
    this will return true
    eg [2, 3, 9]
      [10, 3, 2]
    tempa= [2,9]
    tempb = [10,2]
    return False no way wher reverse is equal to other.
"""

def solution(a, b):
    
    
    if len(a)!= len(b):
        return False
    
    tempa = []
    tempb = []
    
    count = 0
    for i in range(len(a)):
        
        if a[i] != b[i]:
            
            count +=1
            tempa.append(a[i])
            tempb.append(b[i])
        if count >2:
            return False
            
        
    return len(tempa) <=2 and  tempa == tempb[::-1]



def solution(a, b):
    #missing edge case
    
    if len(a) != len(b):
        return False
    unique = {}
    count = 0
    for i in range(len(a)):
        
        if a[i] != b[i]:
            
            if a[i] in unique:
                
                if unique[a[i]] != b[i]:
                    return False
                count+=1
            else:
                unique[a[i]] = b[i]
                unique[b[i]] = a[i]
                count+=1
                if count > 2:
                    return False
    print(unique)
    return count <=2 and len(unique)<=2