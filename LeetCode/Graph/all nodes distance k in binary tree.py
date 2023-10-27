"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
"""

"""
teh way I approached this problem was fist observe that the distance
from any given node is not only a downards traversal of the binary tree but also upwards. therefore UI used depth first search to first create two
adjacency lists one for all nodes pointing upwards and one for all nodes pointing downwards. then I used breadth first search to travel out bidirectionally from the given node using a tuple with node val and distance. I use a set to mark visited nodes. if the condition is met where distance is equal to k we do not append the node val to queue and instead append to results.
the solution below my one is more or less the same thing but a more efficient implmentation of it.
"""

from collections import defaultdict
from collections import deque








class TreeNode:
     def __init__(self, x):
         self.data = x
         self.left = None
         self.right = None
root = TreeNode(3)
r2 = TreeNode(5)
r3 = TreeNode(1)
r4 = TreeNode(6)
r5 = TreeNode(2)
r6 = TreeNode(0)
r7 = TreeNode(8)
r8 = TreeNode(7)
r9 = TreeNode(4)

root.left =r2
root.right=r3
r2.left = r4
r2.right = r5
r3.left = r6
r3.right = r7
r5.left = r8
r5.right = r9

def distanceK(root, target, k):

        upwards = defaultdict(list)
        downwards = defaultdict(list)

        def dfs(root):
            if not root:
                return
            if root.left:
                downwards[root.val].append(root.left.val)
                upwards[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                downwards[root.val].append(root.right.val)
                upwards[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        visited= set()
        queue = deque()
        distance = 0
        queue.append((target.val,distance))
        results = []
        if k == 0 :
            return [target.val]
        while queue:
            traverse = len(queue)
            for i in range(traverse):
                cur,dist = queue.popleft()
                if  cur in upwards:
                    for j in range(len(upwards[cur])):
                        if dist+1 == k and upwards[cur][j] not in visited:
                            results.append(upwards[cur][j])
                        else:
                            if upwards[cur][j] not in visited:
                                queue.append((upwards[cur][j], dist+1))
                if cur in downwards:
                    for j in range(len(downwards[cur])):
                        if dist+1 == k and downwards[cur][j] not in visited:
                            results.append(downwards[cur][j])
                        else:
                            if downwards[cur][j] not in visited:
                                queue.append((downwards[cur][j], dist+1))
                visited.add(cur)
        return results





class Solution:
    def distanceK(root, target, k):
        def build_graph(node, graph, parent):
            
            if node is None:
                return

            if parent:
                graph[node].append(parent)

            if node.left:
                graph[node].append(node.left)
                build_graph(node.left, graph, node)

            if node.right:
                graph[node].append(node.right)
                build_graph(node.right, graph, node)


        graph = defaultdict(list)
        build_graph(root, graph, None)
        result = []
        visited = set()

        queue = deque([(target, 0)])

        while queue:
            n, distance = queue.popleft()
            visited.add(n)

            if distance == k and n:
                result.append(n.val)

            for node in graph[n]:
                if node not in visited:
                    queue.append((node, distance+1))

        return result