"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 
"""
"""
The approach iused was to have two pointers a step 1 one loop through linked list and append each value to a stack. step 2 loop again through the linked list witrh a second pointer and compare if value at slow pointer is equal to last value of the stack.

Another way to do this  and way more elgant is the the solution at the bottom. the idea is to use various pointers to essentially split the linked list into two. this is done with the fast pointer iterating at next.next. if fast is equal to none then the length of the linked list is even. if it is to the last value then the length of the linked list is odd. since you can have an odd palindrome and even palindrome
you jsut have to set the slow node to slow .next if there are odd number of nodes int he linked list. After that its just a case of checking if the two separated lists are equal to each traversing at each point.
"""


def isPalindrome(head):

        slow = head
        fast = head
        stack = []
        while fast.next:
            stack.append(fast.val)
            fast= fast.next
            
        
        stack.append(fast.val)
        
        while slow.next:
            
            
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True


def isPalindrome(head):
        pre = None
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt
        
        right = slow
        if fast:
            right = slow.next
        
        while pre:
            if (pre.val != right.val):
                return False
            pre = pre.next
            right = right.next
        return True