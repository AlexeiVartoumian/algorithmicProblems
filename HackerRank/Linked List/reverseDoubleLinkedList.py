"""
Given the pointer to the head node of a doubly linked list, reverse the order of the nodes in place. That is, change the next and prev pointers of the nodes so that the direction of the list is reversed. Return a reference to the head node of the reversed list.

Note: The head node might be NULL to indicate that the list is empty.

Function Description

Complete the reverse function in the editor below.

reverse has the following parameter(s):

DoublyLinkedListNode head: a reference to the head of a DoublyLinkedList
Returns
- DoublyLinkedListNode: a reference to the head of the reversed list
eturn a reference to the head of your reversed list. The provided code will print the reverse array as a one line of space-separated integers for each test case.

Sample Input

1
4
1
2
3
4
Sample Output

4 3 2 1 
"""
"""
reversing a doubly linked list is easier than reversing a singly linked list.since there is a reference to 
the previous node and the next node its just a case of literally swapping the pointers and moving along the chain
"""
def reverse(llist):
    # Write your code here
    
    temp = llist.next
    
    while temp :
        temp = llist.next
        llist.next = llist.prev
        llist.prev = temp
        if temp :
            llist = temp
    return llist