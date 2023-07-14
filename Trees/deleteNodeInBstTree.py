"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
"""
"""
the first thing to consider is traversing the bst and at every step determine if cur val is less or greater than key. keep doing until key has been found. if key not found then return root unchanged. as such the complexity of the problem lies in what if for a given key it has left and right children. 
if it only has one child then replace it with the other child. since every subtree of a bst is itself also a bst , if there are two children of a given key , then the idea is to manipulate the properties of a bst- we want to repalce the key with the right childs smallest value. this will still be a bst
"""
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root: # if given an empty tree or key not found then return unchanged tree
            return root

        if key > root.val:
            # assigning root.right its child node important because in the event the key is found then the else block on the next function 
            #call will handle reassigning the parent nodes bst subtree. the same is for left 
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            #handle instance where key node only has one child. if so then assign opposite child to respect properties of bst
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # the idea here is to find the smallest value such that is larger then the key. to do this find the left most child of the right subtree of key. this will respect the properties of the bst
            cur = root.right

            while cur.left:
                cur = cur.left
            
            root.val = cur.val
            #now there is a duplicate value within the bst. all that needs to be done is to repeat the function on the root.right subtree to delete that value.
            root.right = self.deleteNode(root.right,root.val)
        return root