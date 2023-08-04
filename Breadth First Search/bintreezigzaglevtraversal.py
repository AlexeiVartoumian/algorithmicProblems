"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
"""
Level order traversal is synonomous with breadth first search. as such to traverse in a zig zag fashion use a boolean to keep track of time to go left or right
for left use python slicing to reverse the list [::-1].
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque()

        left = False
        res = []
        queue.append(root)
        
        while queue:
            traverse = len(queue)
            temp =[]
            for i in range(traverse):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if temp:

                if left:
                    res.append(temp[::-1])
                    left = False
                else:
                    left = True
                    res.append(temp)
        return res
