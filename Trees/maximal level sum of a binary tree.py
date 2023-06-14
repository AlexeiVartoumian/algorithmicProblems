"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 
"""

"""
classic bfs. watch out for if all values in the binary tree are negative.
"""


from collection import deque
def maxLevelSum(root):

        maxsum = float("-inf")
        level = 1
        res = 1
        queue = deque()
        queue.append(root)
        changed = False
        while queue:
            traverse = len(queue)
            temp = 0
            for i in range(traverse):

                cur = queue.popleft()
                if cur:
                    temp+=cur.val
                    queue.append(cur.left)
                    queue.append(cur.right)
                    changed = True
            
            if changed and temp > maxsum:
                maxsum = temp
                res = level
            level+=1
            changed = False
        
        return res

def maxLevelSum(root):
        q = deque([root])

        max_sum = float('-inf')
        level = 1
        max_level = 1
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1

        return max_level