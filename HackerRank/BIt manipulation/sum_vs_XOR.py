"""
Given an integer , find each  such that:

where XOR denotes the bitwise XOR operator. Return the number of 's satisfying the criteria.

Example

There are four values that meet the criteria:

Return .

Function Description

Complete the sumXor function in the editor below.

sumXor has the following parameter(s):
- int n: an integer

Returns
- int: the number of values found

4
"""
"""
the question is a combinatorial question. its basically asking how many possible combination are there such that wherever there is a 0 in the first digit there are ones in the other which is xor. thus all possible combinations will be the number of zeroes to the power of 2. 
"""

def sumXor(n):
    # Write your code here
    
    return 2** bin(n)[3:].count("0")