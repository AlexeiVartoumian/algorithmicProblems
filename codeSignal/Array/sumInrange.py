"""
You have an array of integers nums and an array queries, where queries[i] is a pair of indices (0-based). Find the sum of the elements in nums from the indices at queries[i][0] to queries[i][1] (inclusive) for each query, then add all of the sums for all the queries together. Return that number modulo 109 + 7.

Example

For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], the output should be
solution(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 6 = 10.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer nums

An array of integers.

Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-1000 ≤ nums[i] ≤ 1000.

[input] array.array.integer queries

An array containing sets of integers that represent the indices to query in the nums array.

Guaranteed constraints:
1 ≤ queries.length ≤ 3 · 105,
queries[i].length = 2,
0 ≤ queries[i][j] ≤ nums.length - 1,
queries[i][0] ≤ queries[i][1].

[output] integer

An integer that is the sum of all of the sums gotten from querying nums, taken modulo 109 + 7.
"""

"""
this is a prefix problem. the idea is to iterate through the array and at every pass store the current computed sum in a respective index.

consider the querie [0,5] for an array of length 5. well that will be the end sum of the array after iterating through it. what about [1,5].
well that would be the sum of the array minus the running sum stored at index zero. what about query [2,4]. that would be the sum stored at index store minus the running sum sum stored at the previous index of 2 which is another way of saying give me the sum of the elements between index 2 and 5
"""


def solution(nums, queries):
    
    
    #this is a prefix problem
    
    
    res = [0] * len(nums)
    
    res[0] = nums[0]
    for i in range(1,len(nums)):
        res[i] += res[i-1]+ nums[i]
    
    
    results = []
    for i,x in queries:
        
        if i == 0:
            results.append(res[x])
        else:
            sumSubtractPrevElements = res[x] - res[i-1]
            results.append(sumSubtractPrevElements)

    return sum(results) % (10 **9 +7)