"""
Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of . If it is, they divide it by . If not, they reduce it by the next lower number which is a power of . Whoever reduces the number to  wins the game. Louise always starts.

Given an initial value, determine who wins the game.

Example

It's Louise's turn first. She determines that  is not a power of . The next lower power of  is , so she subtracts that from  and passes  to Richard.  is a power of , so Richard divides it by  and passes  to Louise. Likewise,  is a power so she divides it by  and reaches . She wins the game.

Update If they initially set counter to , Richard wins. Louise cannot make a move so she loses.

Function Description

Complete the counterGame function in the editor below.

counterGame has the following parameter(s):

int n: the initial game counter value
Returns

string: either Richard or Louise
Input Format

The first line contains an integer , the number of testcases.
Each of the next  lines contains an integer , the initial value for each game.

Constraints

Sample Input

1
6
Sample Output

Richard
Explanation

As  is not a power of , Louise reduces the largest power of  less than  i.e., , and hence the counter reduces to .
As  is a power of , Richard reduces the counter by half of  i.e., . Hence the counter reduces to .
As we reach the terminating condition with , Richard wins the game.
"""

"""
given n keep bitshifting 1 to the left until the next power is greater then cur val of n. if this val == n then n is power of two aso divide. else return n - greatest power of 2 less than n. keep flipping boolean that keeps track of whose turn. return Boolean
"""

def counterGame(n):
    #write your code here

    flip = True #if flip true then Richard else louise

    def poweroftwo(n):
        
        power = 1

        while power * 2 <= n:

            power <<=1
        
        if power == n:
            return int(n/2)
        return n- power

    while n!= 1:

        n = poweroftwo(n)
        if flip:
            flip = False
        else:
            flip = True

    if flip:
        return "Richard"
    return "Louise"