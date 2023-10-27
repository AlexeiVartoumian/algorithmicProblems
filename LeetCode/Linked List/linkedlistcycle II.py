"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
    3-->2 --> 0 --> -4
        ^             |
        |             |
        --------------v
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
Example 2:

     1 -->2
     ^   |
     |___v
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
Example 3:

1
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
"""

"""
Tyhe approach here is to have two pointers. one that is slow that traverses the list one node at a time and another that moves fast , twice as fast as in fast = fast.next.next. If there is no cycle fast.next or fast.next.next will eventually hit none. If there is a cycle it is guranteed that slwo and fast wil eventually meet.
After this its simply a case of initialising a third pointer that starts at head and iterates that pointer along with fast only fast now increments as fast.next .
when the two pointers meet that will be the starting point of the cycle.

Another much more simpler method is to store all iterations in a set which means we only care about unique values if at any point our current node is in the set then return that node!
"""
def linkedlistcycleii(head):

    if  head == None or head.next == None or head.next.next == None:
        return

    slow = head
    fast = head
    while slow and fast:
        if fast.next == None or fast.next.next == None:
            return

        if slow == fast:
            slowsecond = head

            while slowsecond != fast:
                slowsecond = slowsecond.next
                fast = fast.next

            return slowsecond

    return 

def linkedlistcycleset(head):
    unique = set()
    cur = head

    while cur is not None:
        if cur in unique:
            return cur
        unique.add(cur)
        cur = cur.next
    return