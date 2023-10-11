"""
you will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

Example
Pick any two elements, say .
Testing for all pairs, the solution  provides the minimum unfairness.
Note: Integers in  may not be unique.
Function Description
Complete the maxMin function in the editor below.
maxMin has the following parameter(s):
int k: the number of elements to select
int arr[n]:: an array of integers
Returns
int: the minimum possible unfairness
Input Format
The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .
Constraints
"""
"""
greedy approach is to sort the array and then making the comparison at turn what is smaller
current max-min of a subsection of array or whatever is soted in the total.
when done making comparison return total.
"""
def maxMin(k, arr):
    # Write your code here
    
    arr.sort()
    
    left = 0
    total = float("inf")
    while left + k <= len(arr):
        
        total = min(total, arr[left+k-1] - arr[left])
        left+=1
    
    return total