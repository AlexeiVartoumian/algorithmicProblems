"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
solution(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""
"""
    this is a prefix sum question where we compute the running sum for every element. at every turn we ask the quesiton running sum minus k index to get thek length running sum    
"""

def solution(inputArray, k):
    
    

    
    indexes = {}
    indexes[-1]  = 0
    runningsum = 0
    curmax = 0
    for i in range(len(inputArray)):
        
        runningsum+=inputArray[i]
       
        if i - k <-1:
            indexes[i] = runningsum
        else:
            indexes[i]= runningsum 
            
            curmax = max(curmax, indexes[i]- indexes[i-k])
    
    return curmax
