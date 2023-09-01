"""
There are two -element arrays of integers,  and . Permute them into some  and  such that the relation  holds for all  where .

There will be  queries consisting of , , and . For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.

Example



A valid  is  and :  and . Return YES.

Function Description

Complete the twoArrays function in the editor below. It should return a string, either YES or NO.

twoArrays has the following parameter(s):

int k: an integer
int A[n]: an array of integers
int B[n]: an array of integers
Returns
- string: either YES or NO

Input Format

The first line contains an integer , the number of queries.

The next  sets of  lines are as follows:

The first line contains two space-separated integers  and , the size of both arrays  and , and the relation variable.
The second line contains  space-separated integers .
The third line contains  space-separated integers .
Constraints

Sample Input

STDIN       Function
-----       --------
2           q = 2
3 10        A[] and B[] size n = 3, k = 10
2 1 3       A = [2, 1, 3]
7 8 9       B = [7, 8, 9]
4 5         A[] and B[] size n = 4, k = 5
1 2 2 1     A = [1, 2, 2, 1]
3 3 3 4     B = [3, 3, 3, 4]
Sample Output

YES
NO
Explanation

There are two queries:

Permute these into  and  so that the following statements are true:

, , and . To permute  and  into a valid  and , there must be at least three numbers in  that are greater than .
"""


"""
After understanding what the problem statement was asking this was way easier, the hardest part for me was exactly that, i thought I would have to do some sort of backtracking algorithm to find all permutations of both arrays.
in the end what the question wants is to make sure all values at a given index is
greater or equal to k , that this must be true for all indexes. after rephrasing my approach was to simply sort both and loop through the start of one and the back of another to see if its possible. 
"""



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    # Write your code here
    
    A.sort()
    B.sort()
    backwards = len(B)-1
    for i in range(len(A)):
        if A[i] + B[backwards] < k:
            return "NO"
        backwards-=1
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()
