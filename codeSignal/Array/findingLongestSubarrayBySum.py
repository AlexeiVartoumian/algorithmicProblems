"""
You have an unsorted array arr of non-negative integers and a number s. Find a longest contiguous subarray in arr that has a sum equal to s. Return two integers that represent its inclusive bounds. If there are several possible answers, return the one with the smallest left bound. If there are no answers, return [-1].

Your answer should be 1-based, meaning that the first position of the array is 1 instead of 0.

Example

For s = 12 and arr = [1, 2, 3, 7, 5], the output should be
solution(s, arr) = [2, 4].

The sum of elements from the 2nd position to the 4th position (1-based) is equal to 12: 2 + 3 + 7.

For s = 15 and arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be
solution(s, arr) = [1, 5].

The sum of elements from the 1st position to the 5th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5.

For s = 15 and arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10], the output should be
solution(s, arr) = [1, 8].

The sum of elements from the 1st position to the 8th position (1-based) is equal to 15: 1 + 2 + 3 + 4 + 5 + 0 + 0 + 0.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer s

The sum of the subarray that you are searching for.

Guaranteed constraints:
0 ≤ s ≤ 109.

[input] array.integer arr

The given array.

Guaranteed constraints:
1 ≤ arr.length ≤ 105,
0 ≤ arr[i] ≤ 104.

[output] array.integer

An array that contains two elements that represent the left and right bounds of the subarray, respectively (1-based). If there is no such subarray, return [-1]
"""


"""
this is a two pointer problem. the idea is to have a running sum that sums up to k where k is the required target. whenever we go over specified amount then shift left pointer until it is equal to right or until the running sum is no longer greate4r than k. if cur sum is equal to target then look at indexes of left and right and compute if the right - left is greater than  the current stored indexes res[1] - res[0]. since here the question states that the index zero is 1 account for this by adding plus 1 to both right and left and the indexes stored in result array if length longer than 1.
"""

def solution(s, arr):
    
    left = 0
    right = 0
    res = [-1]
    runningsum = 0
    while right < len(arr):
        
        runningsum+= arr[right]
        
        if runningsum == s:
            if len(res) == 1:
                res = [left+1, right+1]
            else:
                if (right +1-left+1 ) > (res[1] - res[0]):
                    res = [left+1,right+1]
        elif runningsum > s:
                
                while left < right and runningsum > s:
                    runningsum -= arr[left]
                    left+=1
                
                if runningsum == s:
                  
                    if len(res) == 1:
                        res = [left+1, right+1]
                    else:
                        
                        if (right +1-left+1 ) > (res[1] + 1 - res[0]+1):
                            res = [left+1,right+1]
                        
        right+=1
    return res