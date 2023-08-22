"""
Two friends like to pool their money and go to the ice cream parlor. They always choose two distinct flavors and they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

Example.  

The two flavors that cost  and  meet the criteria. Using -based indexing, they are at indices  and .

Function Description

Complete the icecreamParlor function in the editor below.

icecreamParlor has the following parameter(s):

int m: the amount of money they have to spend
int cost[n]: the cost of each flavor of ice cream
Returns

int[2]: the indices of the prices of the two flavors they buy, sorted ascending
Input Format

The first line contains an integer, , the number of trips to the ice cream parlor. The next  sets of lines each describe a visit.

Each trip is described as follows:

The integer , the amount of money they have pooled.
The integer , the number of flavors offered at the time.
 space-separated integers denoting the cost of each flavor: .
Note: The index within the cost array represents the flavor of the ice cream purchased.

Constraints

, ∀ 
There will always be a unique solution.
Sample Input

STDIN       Function
-----       --------
2           t = 2
4           k = 4
5           cost[] size n = 5
1 4 5 3 2   cost = [1, 4, 5, 3, 2]
4           k = 4
4           cost[] size n = 4
2 2 4 3     cost=[2, 2,4, 3]
"""

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

"""
    #this is a two sime problem . because i am looking for two numbers that have to sum up to money and i cannot
    I cannot laso have a negative sum as in the ice cream man will pay one of the friends to give an ice cream my approach is to simply subtract the given number in the array
    from money. if that number exists then we have two numbers that sum to m. return the index at which they are found
    """ 

def icecreamParlor(m, arr):
    # Write your code here
    complement = {}
    
    money = m
    results = []
    
    for i in range(len(arr)):
        comp = m -arr[i]
        if arr[i] in complement:
            
            results = [complement[arr[i]]+1,i+1]
        else:
            if comp >=1:
                complement[comp] = i
        
    return results