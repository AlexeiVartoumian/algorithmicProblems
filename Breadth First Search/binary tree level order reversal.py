"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""
"""
the questions wanta nodes to be printd level by level . each level is to be sorted into its own array. because of this we need to implement a classic breadth first search only with a queue. the way this works is as follows. step1 : add first element to queue. step 2: keep repeating the following procedure until the queue is empty. step3: whatever the length of the queue is , is how many nodes are at that level, for instance on the first level we will iterate once and do the following. step4. remove the current node from the queue. step5: check if it is not a null value.
step6: if it is a value then append its data into a currentlevel array . step7 append its children to the queue- these will be visited on the next intialisation of step 3 which represents whichever level we are at. step 8: finally check that we are not on the bottom of the tree , as in the current level does not contain null values.
"""
import collections
def levelOrder( root) :

        queue = collections.deque()
        results = []

        queue.append(root)

        while queue:
            traverse = len(queue)
            currentlevel = []
            
            for i in range(traverse):
                node = queue.popleft()
                if node: # this check ensures that null values are never added to current level array
                    currentlevel.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if currentlevel:# this checks that the leaf nodes are not null
                results.append(currentlevel)

        return results