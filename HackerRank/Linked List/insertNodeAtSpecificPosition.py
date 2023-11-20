"""
Given the pointer to the head node of a linked list and an integer to insert at a certain position, create a new node with the given integer as its data attribute, insert this node at the desired position and return the head node.

A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer given may be null meaning that the initial list is empty.
Example
head refers to the first node in the list 
list 1 -> 2-> 3
data = 4
position = 2


Insert a node at position 2 with data = 4. The new list is
1->2->4->3 
"""

"""
need a dummy to handle cases where we are inserting at the start. in the case that happens return the newly made node
with its next valur as head. 
otherwise traverse the list to hit the specific insertion reqiured.
"""

class SinglyLinkedListNode():

    def __init__(self,value):
        self.value = value
        self.next = None
def insertNodeAtPosition(llist, data, position):
    # Write your code here
    
    value = SinglyLinkedListNode(data)
    count = -1
    dummy = SinglyLinkedListNode(1)
    dummy.next = llist
    traverse= dummy
    if count == 0:
        value.next = llist
        return value
    while count != position:
        
        if count+1 == position:
            temp = traverse.next
            traverse.next = value
            value.next = temp
        count+=1
        traverse = traverse.next
    return llist