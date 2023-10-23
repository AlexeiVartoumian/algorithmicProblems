"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height :
        1
      /   \
     2     3
    / \  /   \
   4   5 6    7
image
Function Description

Complete the getHeight or height function in the editor. It must return the height of a binary tree as an integer.

getHeight or height has the following parameter(s):

root: a reference to the root of a binary tree.
Note -The Height of binary tree with single node is taken as zero.

Input Format

The first line contains an integer , the number of nodes in the tree.
Next line contains  space separated integer where th integer denotes node[i].data.

Note: Node values are inserted into a binary search tree before a reference to the tree's root node is passed to your function. In a binary search tree, all nodes on the left branch of a node are less than the node value. All values on the right branch are greater than the node value.

Constraints



Output Format

Your function should return a single integer denoting the height of the binary tree.
"""

"""
practising tree traversal here. below I have the recursive and non recusrive solutions where in the non-recursive solution use level order traversal with breadth first search. in the recursive solution use dfs where two values are stored in array and are incremented/mutateed whenever a call to either lefgt child or right child is possible so as to return the maximum of that array. whenever its not possible to traverse downwards then on that function call decrement.
"""

from collections import deque
def height(root):
    
    
    queue =deque()
    height = 0
    
    queue.append(root)
    
    while queue:
        
        length = len(queue)
        
        for i in range(length):
            cur = queue.popleft()
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        if queue:
            height+=1
    
    return height



def height(root):
    
    values = [0,0]
    if root:
        values[0]+= height(root.left)+1
        values[1] += height(root.right)+1
    else:
        return -1
    
    return max(values)
    