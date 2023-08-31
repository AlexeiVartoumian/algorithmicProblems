"""
Given an array of integers and a positive integer , determine the number of  pairs where  and  +  is divisible by .

Example



Three pairs meet the criteria:  and .

Function Description

Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array 
int ar[n]: an array of integers
int k: the integer divisor
Returns
- int: the number of pairs

Input Format

The first line contains  space-separated integers,  and .
The second line contains  space-separated integers, each a value of .

Constraints

Sample Input

STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]
Sample Output

 5
Explanation

Here are the  valid pairs when :
"""
"""
at first i thought the problem wanted unique divisble pair sums but it doesnt. simple comparison loop works here
"""



def divisibleSumPairs(n, k, ar):
    # Write your code here
    res = 0
    for i in range(len(ar)-1):
        for j in range(i+1,len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                 res+=1
    return res