"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
            1
           / \
          2   3
         / \  
        4   5
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
"""

"""
use an init function that will keep track of the recursive max at every function call. similar to find if a binary tree is balanced use
depth first search to find the deepest node and then recursively check if the distance between one node and another node is greather than the current max.
"""
class TreeNode:
     def __init__(self,  val):
         self.val = val
         self.left = None
         self.right = None
class Solution:

    def __init__(self): # this init function will be used to constantly see what is the larget path value in the binary tree
        self.max = 0
    def diameterOfBinaryTree(self, root):

        
        def diam(self,root): # self needs to be taken as a parameter because we will be returning the self.max arguement which is an integer 

            if root == None:
                return 0 # if there are no children to traverse then we have reached the bottom of a node

            left,right = diam(self,root.left),diam(self,root.right) # hit leftmost node first

            if left+right > self.max: #this line works only because we will be returning an integer this is the comparison we will be making
                self.max = left+right #update if so
             
            return max(left,right)+1 # as we are checking every node in relation to another we will always add 1 as to the distance
        # of one node in relation to another until the base case has been reached.
        
        diam(self,root)
        return self.max



class Solution:

    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root) -> int:

        def diam(self,root):

            if root == None:
                return 0
            
            left,right = diam(self,root.left),diam(self,root.right)

            if left+right > self.max:
                self.max = left+right
            
            return max(left,right)+1

        diam(self,root)
        return self.max 