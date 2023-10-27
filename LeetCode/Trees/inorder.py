"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
"""

"""
to traverse a binary tree in inorder traversal the idea is to access all of the left children of the binary tree first afterwhich you access the root node and finally all of the right children of the binary tree. be careful to remember that as you make a function vall on each node that you are checking the left children first of EACH node therefore given the bianry tree below:
                1
               / \
              2   3
             / \ / \
            4  5 6  7
the in order traversal will be 1,2,4,5,6,3,7 as the function call will start at root 1 move down to 2 and then 4 then it will go back up one to root two and return the right child as root val has already been traversed and then the root node itself will be printed. the same idea happens on the right subtree of the root node. first 6 is printed followed by the hiearachachal right nodes
"""
class Solution:
    def inorderTraversal(self, root) :

        res = []
        def traverse(root,res):

            if root == None:
                return
            
            traverse(root.left,res)
            res.append(root.val)
            traverse(root.right,res)
        
        traverse(root,res)
        return res