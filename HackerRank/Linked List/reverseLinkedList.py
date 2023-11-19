"""
Given the pointer to the head node of a linked list, change the next pointers of the nodes so that their order is reversed. The head pointer given may be null meaning that the initial list is empty.
Example:

head refrences the list
1->2->3->Null
manipulate the next pointes of each node in place and return head , no referncing the head of the list
3 -> 2-> 1 -> NULL.
"""


"""
as per the description its all about  manipulating the pointers.
as such this can be done recurseively but I like the 
iterative solution where a dummy varibale is used so as to swap 
the pointers in place and move along the chain
"""

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    
    dummy = None
    while llist:
        temp = llist.next
        llist.next = dummy
        dummy = llist
        llist = temp
        
    return dummy