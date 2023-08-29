"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

Example


There are three values that differ by : , , and . Return .

Function Description

Complete the pairs function below.

pairs has the following parameter(s):

int k: an integer, the target difference
int arr[n]: an array of integers
Returns

int: the number of pairs that satisfy the criterion
Input Format

The first line contains two space-separated integers  and , the size of  and the target value.
The second line contains  space-separated integers of the array .

Constraints

each integer  will be unique
Sample Input

STDIN       Function
-----       --------
5 2         arr[] size n = 5, k =2
1 5 3 4 2   arr = [1, 5, 3, 4, 2]
"""

"""
since each integer will be unique we want to have constant lookup time when making the calculation does the differnce value pair exist such that it sums to k? so turn the array into a set.
after that iterate thorugh the all the numbers present and with constant lookup time see if current number + k = to number present in the list which is the same as saying number - current number = k
"""
def pairs(arr,k):
    number = set(arr)

    results = 0
    for i in number:
        if i+ k in number:
            results+=1
    return results