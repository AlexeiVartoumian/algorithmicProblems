"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

"""
"""
the trivial answer is to implemnt inorder traversal into the function helpers. however the process can also be done iteratively using a stack where stack become part of the constructor. then it follows the structure of the binary search tree where it will consistently append the left node to the stack structure. the next function will check the current node of stack and pop it . then it checks right of current node and then the left of the current node return the val. finally the has next iterator only has to check if the stack is empty.
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val
    def hasNext(self) -> bool:
        return self.stack != []
        