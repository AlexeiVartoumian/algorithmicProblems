"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
"""

"""
The question is worded in an ambiguous way , but the tip helped out you basically want to traverse the tree keeping track of the current maximum you have encountered at every traversal. use dfs and an array iwith single value that incremeents whenever the value is greater.
"""

def goodnode(root):

    value = None
    if not root:
        return value
    
    value =root.val
    results = [0]

    def dfs(root,value):

        if root:

            if root.val >= value:
                results[0]+=1
            value = max(value,root.val)
            dfs(root.left,value)
            dfs(root.right,value)
    
    dfs(root,value)
    return results[0]

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        value = None
        if not root:
            return value
        
        results = [0]
        value = root.val
        def dfs(root,value):

            if root:
            
                if root.val >= value:
                    results[0]+=1
                value = max(value,root.val)
                dfs(root.left,value)
                dfs(root.right,value)
        
        dfs(root,value)
        return results[0]