"""
"""




"""
The approach I took was to always take the middle value of the list and turn that into a root of BST. after that split the list into left and right of the middle element. after that it is a case of repeatedly taking the middle element from the left and the right of the arrays and sorting them into the bst. However the problem with this is that there are instances where it will not create a balanced binary search tree.

The actual approach is to use a divide and conquer algorithm which is recursive. using a left pointer and a right pointer to constantly find the middle point of all left children of root node and all right children of middle node. the base case is if at any time the left pointer becomes greater than the right pointer as in we have looked at all elements in that section of the sorted array.the recursive solution is directly below
"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def sorted(nums):
     
    def helper(left,right):
            if left > right:
                return None

            middle = (left+right)//2

            root = TreeNode(nums[middle])

            root.left = helper(left,middle-1)
            root.right = helper(middle+1,right)
            return root
    return helper(0,len(nums)-1)

def sortedArrayToBST(nums):
        left = []
        right = []
        root = None
        if len(nums) >= 3:
            
            left = nums[:(len(nums)//2):]
            right = nums[(len(nums)//2)+1:]
            root = TreeNode(nums.pop(len(nums)//2))
            
            cur1 = root
            
            while left:
                    r = TreeNode(left.pop(len(left)//2)) 
                    while cur1:
                        if r.val <= cur1.val:
                            if not cur1.left:
                                cur1.left = r
                                break
                            else:
                                cur1 = cur1.left
                        elif r.val > cur1.val:
                            if not cur1.right:
                                cur1.right = r
                                break
                            else:
                                cur1 = cur1.right
                    
                    
                    cur1 = root
            while right:
                    r = TreeNode(right.pop(len(right)//2)) 
                    while cur1:
                        if r.val <= cur1.val:
                            if not cur1.left:
                                cur1.left = r
                                break
                            else:
                                cur1 = cur1.left
                        elif r.val > cur1.val:
                            if not cur1.right:
                                cur1.right = r
                                break
                            else:
                                cur1 = cur1.right
                                 
                    cur1 = root
                    
        else:
            root = TreeNode(nums.pop(0))
            while nums:
                root.right = TreeNode(nums.pop())
            
        return root
