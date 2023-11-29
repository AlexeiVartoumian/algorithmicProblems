"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

example: 
h1 = [1,2,1,1]
h2 = [1,1,2]
h3 = [1,1]

there are 4,3,2 cylinders in the three stacks, with their heights in the three arrays. Remove the top 2 cylinders from  h1 (heights = [1, 2]) and from  h2 (heights = [1, 1]) so that the three stacks all are 2 units tall. Return 2 as the answer.

Note: An empty stack is still a stack.
Sample Input

STDIN       Function
-----       --------
5 3 4       h1[] size n1 = 5, h2[] size n2 = 3, h3[] size n3 = 4  
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]

output = 5
to equalise remove 3 from stack1 4 from stack2 and [1,1] from stack 3.
"""

"""
The first thing to note here is that the top of the stack for this question
is the beginning index for each array. the rule is that the largest sum of any given stack dictates the order in which to remove values. so long as a given stack is higher than any other then cylinders must be removed from until this is no longer true. keep removing until all values are equal or until one of the stacks are empty which means return zero. 
"""

def equalstacks(h1,h2,h3):

    h1sum = sum(h1)
    h2sum = sum(h2)
    h3sum= sum(h3)

    while h1 and h2 and h3:

        if h1sum == h2sum== h3sum:
            return h1sum
        while h1 and h1sum > h2sum:
            h1sum-= h1[0]
            h1.pop(0)
        while h2 and h2sum > h3sum:
            h2sum-= h2[0]
            h2.pop(0)
        while h3 and h3sum > h1sum:
            h3sum-= h3[0]
            h3.pop(0)
    return 0
        