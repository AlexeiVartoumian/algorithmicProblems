"""
Given pointers to the heads of two sorted linked lists, merge them into a single, sorted linked list. Either head pointer may be null meaning that the corresponding list is empty.

Example
 refers to 
 refers to 

The new list is 

Function Description

Complete the mergeLists function in the editor below.

mergeLists has the following parameters:

SinglyLinkedListNode pointer headA: a reference to the head of a list
SinglyLinkedListNode pointer headB: a reference to the head of a list
Returns

SinglyLinkedListNode pointer: a reference to the head of the merged list
Input Format

The first line contains an integer , the number of test cases.

The format for each test case is as follows:

The first line contains an integer , the length of the first linked list.
The next  lines contain an integer each, the elements of the linked list.
The next line contains an integer , the length of the second linked list.
The next  lines contain an integer each, the elements of the second linked list.

Constraints

, where  is the  element of the list.
"""

"""
this uses the merge procedure from merge sort. to avoid a whole bunch of possible edge cases with one of the input linked lists not being intialised use a dummy node and from there on take advantage of the proerties of a sorted list. 

for example if there is no head1 but there is head2 at the first pass then return head2 and vice versa. otherwise using the above as a golden rule just use the merge procedure whre at every step append the smaller/equal of the the two heads.
finally if the end of one list is reached append the entire head of the other list to the dummy traversal node list. return dummy .next when done.
"""

class singlyLinkedListNode():
    def __init__(self,val):
        self.val = None
        self.next = None

def mergetwosortedlinkedlists(head1,head2):

    dummy = singlyLinkedListNode(0)
    traversal = dummy

    if not head1:
        return head2 # return merged head2 list since None and either sorted list or none will be merged
    if not head2:
        return head1
    while True:
        if not head1:
            traversal.next = head2
            break
        if not head2:
            traversal.next = head1
        if head1.val <= head2.val:
            traversal.next = head1
            head1 = head1.next
            traversal = traversal.next
        elif head2.val < head1.val:
            traversal.next = head2
            head2 = head2.next
    
    return dummy.next
    
