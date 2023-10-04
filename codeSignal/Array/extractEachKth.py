"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
"""


"""
using slice functionality starting at k-1 to account for zero index and stepping through the array every k element. or use auilary array not appending whenver kth element occurs
"""

def solution(inputArray, k):
    del inputArray[k-1::k]
    return inputArray




def solution(inputArray, k):
    
    
    res = []
    
    count = 0
    for i in range(len(inputArray)):
        
        count+=1
        if count == k:
            count = 0
        else:
            res.append(inputArray[i])
    
    return res