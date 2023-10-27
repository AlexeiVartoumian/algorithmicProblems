"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

"""
This probem is basically the same as subsets 1 with a check firrst sort the numbers. after this make sure that if current index is ahead of the combo index
and they are the same value then skip it.
"""
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        nums.sort()

        res= []
        res.append([])

        def backtrack(start,combo):
            
            if start == len(nums): #base condtion to backtrack
                return
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]: # add combo's going forward never backward
                    continue
                combo.append(nums[i])
                res.append(combo.copy())
                backtrack(i+1,combo) # i+1 for start variable helps us look at diff perms of a list
                combo.pop() # backtrack

        backtrack(0,[])
        return res
def subsetsnodups(nums):

    results = []
    nums.sort()
    def backtrack(nums,start,path,results):

        results.append(path)

        for i in range(start,len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(nums, i+1,path+ [nums[i]],results)
    
    backtrack(nums,0,[],results)
    return results

def subsetsWithDup(nums):

        nums.sort()
        results =[]

        def backtrack(nums, start, path, results):

            results.append(path)

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                backtrack(nums,i+1,path+[nums[i]],results)
        
        backtrack(nums,0,[],results)
        return results