"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

 
Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
"""

"""
ob1: a leaf by definition is a node that has no children. therefore

dfs preorder. call all left children and then call all right children since we only want the lead nodes. when leaf node is reached append to list.
keep going until the while tree is traversed. do the same for the next tree.
return if boolean based on if both lists are equal.
"""

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        
        res1 = []
        res2 = []
        def dfs(root,res):


            if root and not root.left and not root.right:
                res.append(root.val)
                return
            elif not root:
                return
            dfs(root.left,res)
            dfs(root.right,res)
        
        dfs(root1,res1)
        dfs(root2,res2)
        return res1 == res2
