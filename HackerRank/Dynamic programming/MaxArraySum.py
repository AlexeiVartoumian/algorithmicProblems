"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset. It is possible that the maximum sum is  0, the case when all elements are negative.

Example
arr = [-2,1,3,-4,5]

The following subsets with more than 1 element exist.These exclude the empty subset and single element subsets which are also valid.

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8
The maximum subset sum is 8.Note that any individual element is a subset as well. arr = [-2,-3,-1]
In this case, it is best to choose no element: return 0.
Function Description

Complete the maxSubsetSum function in the editor below.

maxSubsetSum has the following parameter(s):

int arr[n]: an array of integers
Returns
- int: the maximum subset sum
The first line contains an integer, n.
The second line contains n spance-seprated integers arr[i].

Constraints:
1<= n <= 10 ^5
-10^4 <= arr[i] <= 10 ^4

Sample Input 0

5
3 7 4 6 5
Sample Output 0

13
Explanation 0

Our possible subsets are
[3,4,5], [3,4],[3,5],[7,6],[6,5],[4,5] The largest subset sum is 13 from subset [7,6]

Sample Input 2

5
3 5 -7 8 10
Sample Output 2

15
Explanation 2

Our subsets are
[3,-7,10], [3,8], [3,10],[5,8],[5,10],[-7,10].
The maximum subset sum is 15 from the fifth subset listed.
"""

"""
At first I misread the question thinking that the sum had to be the largest alternating sum in which case apply kadanes algorithm to whenever i % 2 == 0 and i % 2 == 1 as odd or even sums. however a given subarray can accept the first and last integers for example assuming they are both positive and everything in between is negative.

as such I knew I wanted to greedily alternate between the the current element in the array , the sum directly which is the element directly before where I could not apply any operations to and the previous element with which I could apply operations to. my approach was to store the largest value in the current index  between prevel + current index and prev el and alternating between the larger of previous element and current element setting the larger of the two to previous element.
in this way I could bubble up the largest alternating sum that is non-adjacent
"""

def maxSubsetSum(arr):
    prevel = 0
    curel = 0
    for i in range(len(arr)):
        arr[i] = max(prevel + arr[i],prevel)
        prevel = max(prevel,curel)
        curel = arr[i]
    return max(prevel,curel,arr[-1])