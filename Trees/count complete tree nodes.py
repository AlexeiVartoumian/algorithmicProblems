"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
"""

"""
i understood this as simply counting the number of treenodes. I used dfs where i return an integer count. as such if node exists increment count for every node that exists. because the dfs function is returning type integer the left child or right child also exists then increment count by 1 for each one that does. return count when finished traversing.
"""

class Solution:

    def countCompleteTreenodes(self, root:Optional[Treenode])->int:

        count = 0

        def dfs(root,count):
            if not root:
                return 0
            
            else:
                count = 1 + dfs(root.left,count) + dfs(root.right,count)
            
            return count



        return dfs(root,count)
