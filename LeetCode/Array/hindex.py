"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1
 
Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

"""
the h-index property dictates that AT THE VERY LEAST if there is only one paper with one citation then the h-index is one. consequently even if that one paper has a million citations the h-index will still be one. therefore the deciding factor for h-index is the number of papers that is the length of the array where the maximum possible h-index is the length of the array.

as such sort the array then iterate through it. at each turn ask the question , is the number of citations greater than zero?
if so then the maximum value for h-index will be either the current h-index OR the MINIMUM between the length of array minus index and current value at that position. at end of loop return h-index.
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:


        hnum = 0
        maxpos = len(citations)
        citations.sort()

        for i in range(len(citations)):

            if citations[i] == 0:
                maxpos-=1
            else:
                hnum= max(hnum, min(len(citations)-i,citations[i]))

        return hnum