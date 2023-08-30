"""
Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

sweetness  Least sweet cookie   2nd least sweet cookie).

This occurs until all the cookies have a sweetness .

Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .
"""

"""
this is a heap problem. a heap is a binary tree like structure that is categorized according value i.e if root is largest value then all of its children will be smaller then it with the leaf of the heap being the smallest values and vice versa for smallest values. to perform operations such as insertin and deletion we apply the "heapify" process where in the case of say deletion  replace the node to be delted with the leaf node. after this the heapify process is applied where starting from the top items are conitunally swapped until the properties of the heap-like structure are satisfied. in this case we want a min heap because we want quick access to the smallest items in order to apply the rule of (a + 2*b) where a and b are the two smallest items in the array. since this turns two elemetns into one keep doing this until top of heap is greater than k or  we have more than one element to apply this op to. 
"""

import heapq

def jesselikescookies(k,A):

    heapq.heapify(A)
    operations = 0

    while A[0] <k and len(A) >1:
        value = heapq.heappop(A) + (2 * heapq.heappop(A))
        heapq.heappush(A,value)
        operations+=1
    
    return operations if A[0] >=k else -1
