"""
Davis has a number of staircases in his house and he likes to climb each staircase 1,2 or 3  steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase, module  on a new line.

Example


The staircase has  steps. Davis can step on the following sequences of steps:

1 1 1 1 1
1 1 1 2
1 1 2 1 
1 2 1 1
2 1 1 1
1 2 2
2 2 1
2 1 2
1 1 3
1 3 1
3 1 1
2 3
3 2
There are  possible ways he can take these  steps and 

Function Description

Complete the stepPerms function using recursion in the editor below.

stepPerms has the following parameter(s):

int n: the number of stairs in the staircase
Returns

int: the number of ways Davis can climb the staircase, modulo 10000000007
"""
""" 
this is the classic dp problem where the question that has to be asked
is how many steps is it possible to traverse when n = 1? wel we know the answer must be one. what about when n = 2? we know that n = 2 means for sure we can take one 2 step but we can also take two one steps. therefore we grab that value from the previous work done and apply it to the current iteration. in other words we are saying the greater n is it will alwyas be the rolling sum 
of the possbile unique combinations that we can traverse.finally when n is equal to three we have a unique combination as in one three step
but we can also do [1,2] [2,1], [1,1] which was previously computed. therefore in dp style apply this computation rule to each iteration working up to n. 
"""
def stepPerms(n):
    # Write your code here
    if n < 4 :
        if n == 1: 
            return 1
        if n == 2: 
            return 2
        if n == 3 : 
            return 4
    records = [0] * n
    
    records[-1] = 1
    records[-2] = records[-1] + 1
    records[-3] = records[-2] + records[-1] + 1
    
    
    
    for i in range(n-4,-1,-1):
        records[i] = records[i+1]+ records[i+2]+ records[i+3]
    
    return records[0]