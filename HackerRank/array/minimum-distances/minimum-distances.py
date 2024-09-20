#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

#run through and store index of last integer with integer as key.
#make min comparison if found and dict and return that
def minimumDistances(a):
    # Write your code here
    distances = defaultdict(int)
    
    actual = len(a)+1
    for index , value in enumerate(a):
        if value not in distances :
            distances[value] = index
        else:
            actual = min(actual , index- distances[value] )
            distances[value] = index
    
    return -1 if actual == len(a)+1 else actual

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
