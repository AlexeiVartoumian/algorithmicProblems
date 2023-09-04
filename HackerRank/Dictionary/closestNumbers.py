
"""
Sorting is useful as the first step in many different tasks. The most common task is to make finding things easier, but there are other uses as well. In this case, it will make it easier to determine which pair or pairs of elements have the smallest absolute difference between them.

Example

Sorted, . Several pairs have the minimum difference of : . Return the array .

Note
As shown in the example, pairs may overlap.

Given a list of unsorted integers, , find the pair of elements that have the smallest absolute difference between them. If there are multiple pairs, find them all.

Function Description

Complete the closestNumbers function in the editor below.

closestNumbers has the following parameter(s):

int arr[n]: an array of integers
Returns
- int[]: an array of integers as described

Input Format

The first line contains a single integer , the length of .
The second line contains  space-separated integers, .
"""
"""
Dicitonary problem. use absolute value as key and append numbers in order as i-1,i.
return that list. complexity of at least n*logn as numbers are sorted first.
"""


from collections import defaultdict
def closestNumbers(arr):
    # Write your code here
    arr.sort()
    
    minimum = float("inf")
    #thinking to store a given absolute difference as the key and a given pair
    #belongs to that key. finally comparison loop.
    theobject = defaultdict(list)
    for i in range(1,len(arr)):
        absdiff= abs(arr[i] - arr[i-1])
        theobject[absdiff].append(arr[i-1])
        theobject[absdiff].append(arr[i])
        minimum = min(absdiff,minimum)
    
    return theobject[minimum]