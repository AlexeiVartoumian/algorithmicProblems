"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
"""
"""
use dfs to traverse the graph to first find p and q. recall that dfs will start at the root and will keep going until a rule is satisfied in this case finding p or q. on the first instance that either p or q is found FOR A GIVEN ROOT that root can only be the lowest common ancestor if and only if both p and q have been found and have a value as in they both exist in the same subtree. therefore we only call dfs recursively on the left and right of a given node. if both left and right have a value then the root must be the lowest common ancestor. otherwius either left or right must be the lowest common ancestor of itself or it will return none as end value since the whole tree will be traversed.
"""
class Treenode:

    def __init__(self, val):
        self.val = val
        self.left= None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root:Treenode,p:Treenode,q:Treenode)->Treenode:

        #traverse the tree and assign the first instance found of p or q to a variable 
        if root == None or root == p or root ==q:
            return root
        
        # the base case will asssign a value to left and right if it finds p or q thi
        left = self.lowestCommonAncestor(root.left,p,q)
        right =self.lowestCommonAncestor(root.right,p,q)

        # if both values have a value then root must be lca of the given subtree
        if left and right:
            return root

        # in case either one is true since lca can be lca of itselfor none at all 
        return left or right