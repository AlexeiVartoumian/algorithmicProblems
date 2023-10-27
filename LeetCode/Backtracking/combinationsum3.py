"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
"""

"""
backtracking! backtracking is used when we want to figure out all the permutations of a given set of conditions in this case a combination sum that is of k length and is between 1-9. the idea is to implement a decision tree for every number between 1 and 9 and ask the following questions. is the sum total of my current combination of numbers less then k? is it also less than the target number? if both are true then we are about to implement a decision tree for that number qne iterate from that number to n. there are two cases to consider when the above questions return a false answer. if our conditions violated i.e the sum is greater than target number or the length of the list is equal to k and is not the total sum then prune the decision tree by popping it off our combination list and continue iterating. the other case is that the current list is of length k and is the required sum in which case add it to the final results list. do this for every number from 1 to 9.
"""


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
    
        def backtrack(combo,curnumber):
            if sum(combo) > n:
                combo.pop()
                return
            elif len(combo) < k:
                combo.append(curnumber)
                if sum(combo) == n and len(combo)== k:
                    res.append(combo.copy())
                    return
                if sum(combo) > n or len(combo)== k:
                    return
            else:
                combo.pop()
                return
            for i in range(curnumber,9):
                backtrack(combo,i+1)
                combo.pop()
        for i in range(1,10):
        
            combo = []
            backtrack(combo,i)
        return res