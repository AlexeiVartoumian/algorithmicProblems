"""
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

"""
this requires a combination of a hashmap to quickly access items and a linked list for constant time delete swapping and grabbing the least used element. the tail element of the list will always be the element always to be deleted making sure to delete all references to a given node that is the forward and backward link
"""

class Node:
    def __init__(self,key:int, value:int, prev =None,next = None):
        self.key: int = key
        self.value: int = value
        self.prev: Optional[Node] = prev
        self.next:Optional[Node] = next


class LinkedList:
    head:Optional[Node] = None
    tail: Optional[Node] = None

    def addtohead(self,item:Node) -> None:
        
        if self.head is not None: 
            item.next =self.head
        if self.tail is None: # first element given
            self.tail = item
        self.head = item
    
    def swap(self,item:Node) -> None:
        if item is None:
            return
        # grab prev and next els to unlink the middle guy
        previtem: Node = item.prev
        nextitem :Node = item.next
        if previtem is not None:
            previtem.next = nextitem
        if nextitem is not None:
            nextitem.prev = previtem
        if self.head == item:
            self.head = nextitem
        if self.tail == item:
            self.tail = previtem
        
        #make double sure to unlink all references to cur element passed in
        item.prev = None
        item.next = None


class lrucache:
    capacity: int
    cachemap: Dict[int,Node]
    reversequeue = LinkedList

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cachemap= {}
        self.reversequeue = LinkedList()
    
    def get(self,key:int) -> int:
        if key not in self.cachemap:
            return -1
        nodevalue: Node = self.cachemap[key]
        if self.reversequeue.head != nodevalue: # no need to unlink head value
            self.reversequeue.swap(nodevalue)
        return nodevalue.value

    def put(self,key:int, value:int)-> None:
        nodevalue: Node = Node(key,value)
        if key in self.cachemap: # in case givern value is being updating all value
            self.removeitem(self.cachemap[key])
        if len(self.cachemap)>= self.capacity:
            self.deleteleastused()
        self.addtohead(nodevalue) # add new instance to front of reverse queue
        self.cachemap[key] = nodevalue # update or include refrence for constant operations in the dicitonary
    
    def deleteleastused(self)-> None:
        lruitem: Node = self.reversequeue.tail # will always be last element in linkedlist
        if lruitem is None:
            return
        self.removeitem(lruitem)
    
    def removeitem(self,item:Node)-> None:
        self.reversequeue.swap(item) # unlink the last element
        del self.cachemap[item.key]
        del item

