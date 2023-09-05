"""
You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

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
Sample Input
Sample Input #01
10
4
1
2
3
4
10
20
30
40
100
200
Sample Output

Sample Output #01

3
Explanation

Explanation #01
Here ; selecting the  integers , unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
"""
"""
Hackerank prompts can be so ambiguous this was so hard for me to decipher. allow me to rephrase . what we want is the minimum diffreence between any two numbers such that have the following properties:
1: there is a range of k numbers between them inclusive.
2: the difference between this max and the min of this group of numbers is the smallest possible , all of which are derived from the original list.

knowing this sort the numbers and taking advantage of the properties of a sorted list do a sliding window of sorts where for each "min and max" value of the k length window compute if that difference is the smallest one
"""

def maxMin(k, arr):
    # Write your code here
    
    results = []
    arr.sort()
    curmin = arr[-1] - arr[0]
   
    for i in range(len(arr)-k+1):
        if arr[i+k-1] - arr[i] < curmin:
            curmin =arr[i+k-1] - arr[i]
    return curmin
    