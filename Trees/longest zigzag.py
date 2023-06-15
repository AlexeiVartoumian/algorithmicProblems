"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
"""

"""
use a boolean to flip out on every diretion and call dfs on the left of the root and the right of the root.
for each traversal treat every node as root where the if elese condition will fire and allow the traversal
in qa zig zag fashion. use self.max length to keep track od the logest zigag found
"""





def longestZigZag(self, root: Optional[TreeNode]) -> int:


        self.maxlength = 0
        def dfs(root, directleft,count):

            if not root:
                return 
            
            self.maxlength = max(self.maxlength,count)

            if directleft:
                dfs(root.right,False,count+1)
                dfs(root.left,True,1)
            else:
                dfs(root.left,True,count+1)
                dfs(root.right,False,1)
        dfs(root,True,0)
        dfs(root,False,0)
        return self.maxlength