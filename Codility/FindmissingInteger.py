"""
Find the smallest positive integer that does not occur in a given sequence.
Task Score
100%
Correctness
100%
Performance
100%
Task description
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""
"""
good practise. this question is riddled with edge cases. Had to come up with these integer  test case lists and sort them to derive:

case 1: 1,1,2,3,4,6 => all positive numbers with a number skipped : return skipped number
case 2: -1,-3 => all negatives : return 1
case 3 : 5,10 => all positives but starting digit greater than 1 : return 1 
case 4: -1,0,1 => mix of negative and positives but last integer is 1 : return 2
case 5: -5 ,100 => mix of neg and pos but there exists a gap between last neg integer and first pos integer >1 and first pos >1 : return 1
case 6 : -5,1,2,300 => mix of neg and pos and first positive is 1 : case becomes identical to case 1 at first positive  
case 7 : 1,2,3 => consecutive positives : return last value plus 1
case 8 : 1 => only one digit and that digit is 1: return 2 (covered by case 4)
case 9: 2 => only one digit and that digit is >1 : return 1 (covered by case 3)

my approach  was to sort the list and knock out all negatives and last integer being 1. cases : 2,4,8,9
after that the rule I applied was that I only wanted to start looking at integers that are positive and the first occuring place where this is true. list has to be sorted. 
check if that first occuring integer is greater than 1 and if so return 1. cases : 3 , 5 
otherwise compare each integer with the one ahead of it to check if there is a skipped number there somewhere. cases : 1,6
if that condition never fires then all conditions have been handled and there exists a consecutive list => return last value + 1. cases: 7
"""

def solution(A):
    # Implement your solution here
    A.sort()
    if A[-1] < 1:
        return 1
    if A[-1] == 1:
        return 2
    if len(A) == 1:
        return 1
    start = 0
    while start < len(A) and A[start] <1:
        start+=1
    if A[start] > 1:
        return 1
    #loop starts at 1
    for i in range(start,len(A)-1):
        if A[i+1] - A[i] > 1:
            return A[i] + 1
    
    return A[-1]+1