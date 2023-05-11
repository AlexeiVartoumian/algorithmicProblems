"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
"""

"""
use a stack to append cur value check if its when its none if it is equal to target sum . other wise keep goin down the left and the right and append a tuple of the node and current value. if stack is empty then while loop will stop executing and return false.

revisited: another option is to use the preorder traversal which starts at the root and then traverses the left anf then right subtree. the idea is to use dfs and return either the left or right traversal which will only be set to true if and only if the both children of a given node are equal to each other .
"""


def pathsum(root,targetsum):

    def dfs(curnode,cursum):
        
        if not curnode:
            return False
        
        cursum += curnode.val
        if curnode.left == curnode.right:
            return cursum == targetsum

        left = dfs(curnode.left,cursum)
        right = dfs(curnode.right,cursum)
        return left or right
    

    return dfs(root,0)


def pathsum(root,targetsum):
    if root == None:
        return False
    
    stack = [(root,0)]

    while stack:
        curnode,cursum = stack.pop()
        cursum+= curnode.val

        if curnode.left == None and curnode.right == None:
            if cursum == targetsum:
                return True
        
        if curnode.left: stack.append((curnode.left,cursum))
        if curnode.right: stack.append((curnode.right,cursum))
    
    return False

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        if root == None:
            return False
        
        stack=[(root, 0)]
        
        
        while stack:
            cur_node,node_sum=stack.pop()
            node_sum+=cur_node.val
            # if the node is leaf node
            if cur_node.left is None and cur_node.right is None:
                if node_sum==targetSum: return True
            if cur_node.left: stack.append((cur_node.left,node_sum))
            if cur_node.right: stack.append((cur_node.right,node_sum))
        return False

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if root == None:return False
        
        return self.hasPathSumHelper(root, targetSum)

    def hasPathSumHelper(self, root, targetSum: int) -> bool:
        if root.right == None and root.left == None:
            if targetSum - root.val == 0:
                return True

            return False
         
        if  root.right and self.hasPathSumHelper(root.right, targetSum - root.val):
            return True
        
        if  root.left and self.hasPathSumHelper(root.left, targetSum - root.val):
            return True

        return False