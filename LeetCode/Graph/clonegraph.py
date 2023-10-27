"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""
"""
approach is moake a copu of the undirected graph by using a dictionary whci will be accessed globally/recursively.use dfs search on the given node. it it existss then obey the structure of the node (node.val , [1,2,3] else []) and do the following: check if it already exists in the dictionary. if yes then avoid duplciates and return the self.dictionary[node]. if not then we need to create a copy of it and then visit all the neighbours. first create a instance of class Node say copy and then store in dicitonary. then loop through  all negihbours of orignal node, append it to the copy instance , calling dfs each time like so copy.neighbours.append(self.clongraph(neighbour)) return copy which will be the first value given orignally.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    def __init__(self):
        self.newgraph = {}
    
    def clonegraph(self,node):

        if not node:
            return None
        
        if node in self.newgraph:
            return self.newgraph[node]

        copy = Node(node.val,[])
        self.newgraph[node] = copy

        for neighbour in node.neighbors:
            copy.neighbors.append(self.clonegraph(neighbour))
        return copy