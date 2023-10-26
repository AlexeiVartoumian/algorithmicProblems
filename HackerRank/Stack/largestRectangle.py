"""Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

Example

A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

k * min(h[i],h[i+1],...,h[i+k-1])
largestRectangle has the following parameter(s):

int h[n]: the building heights
Returns
- long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings

Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each the height of a building.

Constraints

Sample Input

STDIN       Function
-----       --------
5           h[] size n = 5
1 2 3 4 5   h = [1, 2, 3, 4, 5]
Sample Output:
9
why so? since the maximum rectangle that is possible to be created such that is bound by the length 
are the numbers 3,4,5 . where 3 is the largest smallest value and that is possible to create a largest rectangle. 
"""

"""
the implementation of this problem compeltely escaped me. my understanding of this problem is that its
a combination of a prefix sum problem and alongside alongside being greedy by index. as such the we need a stack to keep track of all the values represented as hieght amd the index at where they sit. the first observation is that if all hieghts were considered than the largest rectangle will be reduced to  the smallest value multiplied by length. imagine the case where all numbers are sorted. at that point its just a prefix sum problem given index 
the rectangle at that point will be that number assigned at that index multiplied by length - up to that index.

the intuition that I lacked was how to handle numbers such that were not sorted. turns out you want to reassign 
the index of the current number to the furthest previous number index so long as its larger than that current number ---> in a greedy like manner popping off all the values in the stack and computing thier values along the way. in the end the calcuations of prefix sums from  length of list minus cur index multiplied by that number will be all thats left to do since the numbers will be sorted.  
"""

def largestRectangle(h):
    # Write your code here
    maxheight = len(h)
    
    maxarea = 0
    
    stack = []
    # i store the index to value to compute
    #in a prefix style the max possible area
    for index , height in enumerate(h):
        #handle the case where current smaller number 
        #has as series of larger numbers before it.
        greedyindex = index
        """
        in the case where current number is smaller than
        previous number than ALLLLL previous numbers will be REDUCED
        down to this smaller number. therefore the idea is
        to first compute the maximum possbile area up to that smaller number
        only considering nuberthat are larger to popping of until 
        prev smaller number is met. if it was equal it would also consider
        all numbers that are erqual to the first number greater than the current number which is not
        what we want we only want to pop off the stack numbers that are greater than
        """
        while stack and stack[-1][1] >=height:
            
            previndex, greaterheight = stack.pop()
            maxarea = max(maxarea, greaterheight*(index - previndex))
            
            greedyindex = previndex
        stack.append((greedyindex,height))
    """
    finally I need to compute the prefix sum consecutively larget numbers
    """
    for index,height in (stack):
        maxarea = max(maxarea, height *(len(h) -index))
    return maxarea