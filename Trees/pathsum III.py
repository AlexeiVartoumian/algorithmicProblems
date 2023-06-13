"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 
Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""

"""
The n squared approach is to traverse every possible path from parent to children and then repeat the process for its children. as such you will need a helper method intialised that will a) keep track of all target path sums and b) the targetsum itself be part of the function. As such the idea is to use a stack and perform dfs on each node of the stack which will require two functions , one for the stack the other for the the path searching. the process works like so
1. add root to stack. 2. while stack append cur nodes children to stack. 3. go through cur node and check every node value plus the current value is equal to the target sum is yes then increment the method self .count. 4. repeat for left and right children. 5. when this whole process is done return the self.count

because the above is treating every node as the root one at a time and traversing its children alot of repeated work is happening. as such a more optimised way is to store each current sum in an object and checking if that number is equal to the targetsum if not store it and if so then increment the self.count with the purpose of avoiding repeated work and traversing the tree in linear time.
"""

class tree():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def pathsum(self,root,targetSum):

        self.count = 0
        self.targetSum = targetSum

        stack = [root]

        while stack:
            top = stack.pop()

            if top:
                stack.insert(0, top.left)
                stack.insert(0,top.right)


            self.traverse(top,0)
        return self.count

    def traverse(self,curnode,cursum):

        if curnode == None:
            return
        cursum+= curnode.val
        if cursum == self.targetSum:
            self.count+=1

        self.traverse(curnode.left,cursum)
        self.traverse(curnode.right,cursum)

class tree():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

r = tree(10)
r.left= tree(5)
r.left.left = tree(3)
r.left.left.left = tree(3)
r.left.left.right = tree(-2)
r.left.right = tree(2)
r.left.right.right = tree(1)
r.right = tree(-3)
r.right.right = tree(11)

class Solution:
    def pathSum(self, root, targetSum):
        cache = {0:1}
        self.ans = 0
        def dfs(node, sumNum):
            if not node: return
            curSum = sumNum + node.val
            if (curSum - targetSum) in cache:
                self.ans += cache[curSum - targetSum]
            cache[curSum] = cache.get(curSum, 0) + 1
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            cache[curSum] -= 1
        
        dfs(root, 0)
        return self.ans
hey = Solution()
hey.pathSum(r,8)
