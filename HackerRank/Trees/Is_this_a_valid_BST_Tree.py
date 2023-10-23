"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
The  value of every node is distinct.

Given the root node of a binary tree, determine if it is a binary search tree.

Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

        3
      /   \
     2     4    => valid bst
    /     / \
    1     5  6 

     3
   /   \
  2     4    => not a valid bst
/  \   / \
1  5   6  7
"""

"""
obeying the rules and properties of a bst the following observations acn be made. at the base level an empty bst is valid bst. further to this all children of a current root to the left must be smaller. likewise all children to the right og the current
root must be greater.the problem therefore is to keep track of all subtrees and the values they have to the left of a given root and all the subtrees to the right of a given root. whenever we descend left then all values must be smaller than the last recorded right value and vice versa whenever we go to the right of a root then it must be greater then then previously recorded left values. as such the idea is that we do two function calls for every root and at every function call update the value at eft or right . if there is nothing to check then an empty bst is a valid bst. as such whenever we go left we update the right child value and ask the question is current value > right if so then false and we also ask the question is the current valye smaller than the left? using two function calls allows to update the values and to check that a innerchild does not violate the overall rule of the bst.
"""


import sys

def validbst(root):

    values = set() # question asks for unique values only
    def checkvalues(root,left,right):

        if not root:
            return True
        
        if root.data < left or root.data > right or root.data in values:
            return False
        values.add(root.data)
        return checkvalues(root.left,left,root.data) and checkvalues(root.right,root.value,right)

    return checkvalues(root, float(-sys.maxsize), float(sys.maxsize)) 