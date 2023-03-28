"""
Given a binary tree, determine if it is 
height-balanced
.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
            3
           / \
          9  20
             / \
            15  7

Input: root = [1,2,6,3,9,null,null,4,5]
Output: false
                1
              /   \
             2     6
            / \     
           3   9     
          / \         
         4   5
"""

"""
Approach here is to use depth first search. the base case is if a root is none then it can only be balanced. return a list of two elements A boolean and the height incurred. for the base case this will be [True,0]. depth first search is another variant of pre-order traversal so the idea is to start from the bottom of a sub tree and work the way up . for example the tree directly above in preorder traverseal will access the nodes in the following order: 4,5,3,9,2,6,1. at every step we compare if absolute value of left minus right is smaller than or equal to one. If that ever occurs we can return False which will be the first element of the array. remeber our base case is returning an element and as such when we actually call the function we need to return a boolean value which will be the 0 element. see the second sentence.
"""


def isBalanced(root):

    def dfs(root): # dfs is pre order traversal - find leftmost node keep goind fown then right and so on tree above is 
        #4,5,3,9,2,6,1
        
        if root == None:
            return [True,0] # return an array bool keeps track of if height is greater than 1 and integer is actual height of a node starting
        #from the very bottom

        left,right = dfs(root.left),dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1 # this is a boolean value if a false occurs at any point the firs part of the variable will bubble this up the call stack, second part is the conditional that can cause this to happen.

        return [balanced , 1+ max(left[1],right[1])] # the 1+ accounts for every tree having a root.
    
    return dfs(root)[0] 

class Tree():
    
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
"""
root = Tree(3)
root.left = Tree(2)
root.right = Tree(3)
root.right.left =Tree(6)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.left.left=Tree(8)
"""
root = Tree(1)
root.left=Tree(2)
root.left.left = Tree(3)
root.left.left.left= Tree(4)
root.left.right = Tree(9)
root.left.left.right = Tree(5)
root.right = Tree(6)

class Solution:
    def isBalanced(self, root):
         
    
        def dfs(root):

            if root == None:
               return [True,0]
            
            left,right = dfs(root.left),dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <=1

            return [balanced, 1+ max(left[1],right[1])]
        
        return dfs(root)[0]