"""
You have a binary tree t. Your task is to find the largest value in each row of this tree. In a tree, a row is a set of nodes that have equal depth. For example, a row with depth 0 is a tree root, a row with depth 1 is composed of the root's children, etc.

Return an array in which the first element is the largest value in the row with depth 0, the second element is the largest value in the row with depth 1, the third element is the largest element in the row with depth 2, etc.
"""
"""
level-order traversal but checking for largest value at each level.
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
from collections import deque
def solution(t):
    
    if not t:
        return []
    queue = deque()
    
    queue.append(t)
    
    res = []
    while queue:
        traverse = len(queue)
        temp =[]
        for i in range(traverse):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            temp.append(cur.value)
        
        largestval = float("-inf")
        for i in temp:
            largestval = max(largestval,i)
        
        res.append(largestval)
    return res