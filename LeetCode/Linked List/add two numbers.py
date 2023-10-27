"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1] 
"""

"""
read the question or rather look at the test cases! the title is misleading, hearing add two numbers you and given two such numbers 2 4 3 and 5 6 4 you would asume you  807 where each digit inhabits the correct position whereas instead we are required to move along both list on place and add the numbers from left to right. in this case use a while loop to iterate across both linked lists while thery are still true, accounting for if a carryvoer is also true, at every step perfrom the calculation from left to right  creating a new node of the final sum linked list. return dummy.next
"""
class ListNode():
    def __init__(self,val):
        self.val = val
        self.next =None
    
def addtwonumbers(l1,l2):

    dummy =ListNode()

    carryover = 0
    cur = dummy

    while l1 or l2 or carryover:

        #first get val
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        #do computation
        value = val1 + val2 + carryover
        carryover = value //10
        value = value %10
        #store in newlist
        cur.next = ListNode(value)

        #move all pointers along accounting for None
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        cur = dummy
        carryover = 0
        while l1 or l2 or carryover:
            #first get val
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            #next do computation
            value = val1 + val2 + carryover
            carryover = value // 10
            value = value %10
            cur.next = ListNode(value)
            #next set the pointers to the next values
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
