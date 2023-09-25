"""
Note: Try to solve this task without using recursion, since this is what you'll be asked to do during an interview.

Given a binary tree of integers t, return its node values in the following format:

The first element should be the value of the tree root;
The next elements should be the values of the nodes at height 1 (i.e. the root children), ordered from the leftmost to the rightmost one;
The elements after that should be the values of the nodes at height 2 (i.e. the children of the nodes at height 1) ordered in the same way;
Etc.
Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": {
            "value": 5,
            "left": null,
            "right": null
        },
        "right": null
    }
}
the output should be
solution(t) = [1, 2, 4, 3, 5].

This t looks like this:

     1
   /   \
  2     4
   \   /
    3 5
"""

#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

"""
bfs level order traversal
"""
from collections import deque
def solution(t):
    
    #this is level order traversal
    
    queue = deque()
    if not t:
        return []
    queue.append(t)
    res = []
    res.append(t.value)
    while queue:
        traverse = len(queue)
        
        for i in range(traverse):
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                res.append(cur.left.value)
            if cur.right:
                queue.append(cur.right)
                res.append(cur.right.value)
    
    return res