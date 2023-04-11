"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

"""
at the bottom was my attempt to implement. now revisited the attempt at the top is mine and it works :) three stages of backtracking
stage 1 = explore that is bound by a condition stage 2 = grab the desired result and stage 3 will be to "backtrack" as in go back to other possible combinations. consider the subset problem. we want all UNIQUE permutations meaning we do not want to visit element twice. implementing
the above steps theresfore whenever we call the function on itself we want to make combos with elements only after the function call element.
once the condition has been reached in this instance we have traverse all possible combos with a given element. the backtracking begins which is
the popping of the elements from the array until we have bubbled up to the call stack where we first made the call. we add a copy of the array as it is always changing 
"""
def subsets(nums):
        

        res = []
        res.append([])
        def backtrack(start,combo):

            if start == len(nums):
                return
            for i in range(start,len(nums)):
                combo.append(nums[i]) #explore
                res.append(combo.copy()) # append copy
                backtrack(i+1,combo)
                combo.pop()
        backtrack(0,[])
        return res
def subsets(nums):

    results = []

    def backtrack(start, path): # iterate through list recursively using start
        results.append(path)

        for i in range(start,len(nums)): # implement a comparison loop
            
            backtrack(i+1, path+ [nums[i]]) # at each stage add the new element to current path with start element used as index
    
    backtrack(0,[])
    return results



def subsets1(nums):

        result = []

        def backtrack(start, path):
            result.append(path)

            for i in range(start,len(nums)):
                backtrack(i+1, path+[nums[i]])
            
        
        backtrack(0,[])
        return result

def subsetsw(nums):
    
    res= []
    res.append(nums.copy())
    if len(nums) == 1:
        
        return [[],[nums[0]]]
    def backtrack(start,combo):
        
         
        res.append(combo.copy())
        print(res)
        if len(combo) == len(nums):
            #res.append(combo.copy())
            return
        while nums:
            combo = []
            cur = nums.pop()
            res.append(combo)
            combo.append(cur)
            for x in range (len(nums)):
                combo.append(nums[x])
                backtrack(cur,combo)
                combo.pop()
    backtrack(None,[])
    print(res)
    return res

  