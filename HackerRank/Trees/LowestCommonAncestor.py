
"""
You are given pointer to the root of the binary search tree and two values v1 and v2. ou need to return the lowest common ancestor (LCA) of 
v1 and v2 in the binary search tree.

       2
     /   \
    1     3
        /   \
       4     5
              \ 
               6
return 3 as lca.
"""


"""
we always know that given a tree the root that is the start and will always be an ancestor. however we ant the lca the lowest common ancestor. therefore we ask the question that given a subtree of the tree , which in itself is also a tree, is the current value equal to v1 or v2? depending on if v1 or v2 is a left child or right child return root for that call as we have found a value when traversing the tree with dfs.

in the case that v1 is on the left of root and v2 is on the right of root we can return root. otherwise v1 or v2 Must be  on the right or left subtree of a given root. this works because all nodes are sub trees as well as being trees themselves so we can traverse and return either the left or right child as soon we find  a given v1 or v2 
"""

'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
  #Enter your code here
  
    if not root:
        return root 
    if root.info == v1 or root.info == v2:
        return root
    left = lca(root.left,v1,v2)
    right =lca(root.right,v1,v2)
    
    if left and right:
        return root
    
    return left or right