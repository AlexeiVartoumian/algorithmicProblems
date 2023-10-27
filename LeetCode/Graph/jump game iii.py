"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
"""

"""
i tried this problem with two adjlists one for possible positive jumps and the other  for possible negative jumps storing index as key  and value pairs. then used dfs on each respective pair returning an integer value thats incremented if 0 is found and returning if that integer greater than zero.  I was failing one test case and I could not figure out why. as such the second approach is simpler and uses a stack. for every index append positive and negative iterations if its possible to jump to that index. then mark the currentone as visited bu mutating array. keep popping of elements in stack so long as stack exists and that value in array is minus 1. if a value in stack is used as index in array and its zero return True. else return false.
"""
from collections import defaultdict

def canReach(self, arr, start):
        index = start
        stack = []
        stack.append(index)
        while stack:
            if arr[index] == 0:
                return True
            temp = [index + arr[index], index - arr[index]]
            for j in temp:

                if j >=0 and j < len(arr) and arr[j] != -1:
                    stack.append(j)
            
            arr[index] = -1

            while stack and arr[stack[-1]] == -1:
                stack.pop()
            if stack:
                index = stack[-1]
        return False
def canReach(self, arr, start):

        poslist = defaultdict(list)
        neglist = defaultdict(list)

        for i  in range(len(arr)):
            if arr[i] + i < len(arr):
                poslist[i].append(i+ arr[i])
            if i - arr[i] < len(arr):
                neglist[i].append(i - arr[i])
        
        visited = set()
        res = 0

        def dfs(poslist,neglist,visited,start,res):

            if start in poslist and start not in visited:
                temp = start
                start = poslist[temp][0]
                visited.add(temp)
                if arr[start] == 0:
                    res+=1
                    return res
                return dfs(poslist,neglist,visited,start,res)

            if start in neglist and start not in visited:
                temp = start
                start = neglist[temp][0]
                visited.add(temp)
                if arr[start] ==0:
                    res+=1
                    return res
                return dfs(poslist,neglist,visited,start,res)
            
            return res
        
        return dfs(poslist,neglist,visited,start,res) > 0