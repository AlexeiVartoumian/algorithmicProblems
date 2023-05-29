"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

        3
      /  \
     9    20
         /  \
        15    7
"""

"""
observation number 1: inorder traversal = left subtree then root then right subtree. postorder = left subtree then right subtree and finally root.
THERFORE THE LAST ELEMENT IN THE POSTORDER ARRAY WILL ALWAYS BE THE ROOT.
CONSEQUENTLY SINCE INORDER IS LEFTSUB THEN ROOT THEN RIGHT SUB ALL THE ELEMENTS TO THE LEFT OF THE INORDER ARRAY BELONG THE THE LEFT SUBTREE OF THAT GIVEN ROOT AND ALL THE ELEMENTS OF IT BELONG TO THE RIGHT. after deducting this the idea is to pop off the last element in the post order array and call it root.
after this find the index of it in the inorder array and use ARRAY SLICING WHERE ALL ELEMENTS TO LEFT OF CUR INDEX ARE root.left and all to the right are root.right. the base case is where the inorder array in the call stack is empty in which case wqe have reached a terminal node.
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def construct(inorder,postorder):

    if not inorder:
        return
    current = postorder.pop(-1)
    root = TreeNode(current)
    index = inorder.index(current)
    root.right = construct(inorder[index+1::],postorder)
    root.left = construct(inorder[:index:],postorder)
    return root

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        if not inorder:
            return
        
        current = postorder.pop(-1)
        root = TreeNode(current)
        index = inorder.index(current)

        root.right = self.buildTree(inorder[index+1::],postorder)
        root.left = self.buildTree(inorder[:index:],postorder)
        return root