
"""
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29 
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2  
Example


The number  is created by concatenating the string   times so the initial .

    superDigit(p) = superDigit(9875987598759875)
                  9+8+7+5+9+8+7+5+9+8+7+5+9+8+7+5 = 116
    superDigit(p) = superDigit(116)
                  1+1+6 = 8
    superDigit(p) = superDigit(8)
All of the digits of  sum to . The digits of  sum to .  is only one digit, so it is the super digit.

Function Description

Complete the function superDigit in the editor below. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

string n: a string representation of an integer
int k: the times to concatenate  to make 
Returns

int: the super digit of  repeated  times
Input Format

The first line contains two space separated integers,  and .

Constraints


"""

"""
I thought the recursive apporoach would be simple enough but I guess the test cases were throwing massive numbers 
so instead take the string version of the number and extract each digit out of it since strings are iterable.
after that while the collective sum of those numbers is greater than a single digit keep appluing that principle
where grab the sum total of the array and then after that set the sumarray to zero. after that since the question wants the single digit sum of the given number multiplied by k if sinlge number * k is less than 9 return that if not apply aboveprocess one last time and reutrn that to get recursive single digit sum.
"""

def superDigit(n, k): 
    arr = [i for i in map(int , n)]
    
    res = 0
    while sum(arr) > 9:
        
        for i in arr:
            res+= i
        
        arr = [i for i in map(int, str(res))]
        res = 0
    
    if sum(arr) * k <= 9:
        return sum(arr) * k
    else:
        arr = [i for i in map (int, str(sum(arr) * k))]
        return sum(arr)