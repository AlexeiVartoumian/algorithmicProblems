"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. Given a pointer to the head of a linked list, determine if it contains a cycle. If it does, return 1 . Otherwise, return 0.
Example

head refers to the list of nodes 1 -> 2 -> 3 -> NULL 

The numbers shown are the node numbers, not their data values. There is no cycle in this list so return 0.

head refers to the list of nodes  1 -> 2 -> 3 -> 1

There is a cycle where node 3 points back to node 1, so return 1.

Function Description

Complete the has_cycle function in the editor below.

It has the following parameter:

SinglyLinkedListNode pointer head: a reference to the head of the list
Returns

int: 1 if there is a cycle or 0 if there is not
Note: If the list is empty,  will be null.
"""
"""
to determine if there exists a cycle two pointers are needed initialised before the head  and pointing to it.
the first pointer traverses the list normally.
the second goes at twice the speed of the first pointer.
if there is a cycle the two pointers will converge at that point.
this is because wherever the cycle occurs for example given the example above it is at point three. it takes three operations for the first pointer to get there. the second pointer however will have moved six steps.
because there is a cycle we can say the linkedlist has a length of three and that therefore the second pointer will now be at the same point since its already traversed the list.
"""
class SinglyLinkedListNode():

    def __init__(self,val):
        self.val = val
        self.next = None

def has_cycle(head):
    
    if not head:
        return 0
    dummy= SinglyLinkedListNode(-1)
    dummy.next = head
    
    slow = dummy
    fast = dummy
    
    while fast.next and fast.next.next:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return 1
    return 0