"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
"""

"""
I apprached this with a breadth first search similar to the level order traversal. the idea is to aonly append the right most value of a current value. in over words its exactly like the level tree order traversal with a modification done on the current level only appending the right most value. the solution right below this is using a dfs approach
"""
from collections import deque
class Solution:
    def rightSideView(root):

        s = set()

        ans = []

        def dfs(root, level):

            if not root:
                return

            if level not in s:
                ans.append(root.val)
                s.add(level)

            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)

        return ans

def rightmostview(root):

    queue = deque()
    vals= []
    queue.append(root)
    while queue:

        traverse = len(queue) # length of queue is how we get the current level of the tree
        currentlevel = []
        for i in range(traverse):
            
            cur = queue.popleft()
            if cur: #if current node is not a leaf then grab the its children which are the level below  do this for all nodes of traverse level see line 52
                queue.append(cur.left)
                queue.append(cur.right)
                currentlevel.append(cur.val)
        
        if currentlevel: #making sure all we have not reached the very bottom 
            hello = len(currentlevel)
            while hello > 0 and currentlevel[hello] == None: #the modification part we want the first not none value found at the currentlevel at the rightmost side
                hello-=1
            vals.append(currentlevel[hello])
    return vals
def rightSideView(root):


        queue = deque()
        queue.append(root)
        vals = []
        while queue:

            traverse = len(queue)
            currentlevel = []
            for i in range(traverse):
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    currentlevel.append(cur.val)
            
            if currentlevel:

                hello = len(currentlevel)-1
                while hello > 0 and currentlevel == None:
                    hello-=1
                vals.append(currentlevel[hello])
        return vals
