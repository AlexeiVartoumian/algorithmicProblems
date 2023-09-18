"""
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.
"""

"""
approached this with a two stacks. since the question wants THE MIRROR then dfs on the root .left and treat that as if it was head node. do the same for head. right.
then  make a custom dfs function for each head .right and head .right travrsing the "opposite" values appending either the value or none to the respective stack. at the end of traversal check if both stacks are equal to each other
"""
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def solution(t):
    
    
    #ill atempt this with two stacks
    #and treat root.left as head1
    #and root.right as head2
     
    stackleft = []
    stackright = []
     
    if not t or not t.left and not t.right:
         return True
    
    def dfsleft(root,stack):
        
        if not root:
            stack.append(None)
            return stack
        else:
            stack.append(root.value)
            dfsleft(root.left,stack)
            dfsleft(root.right,stack)
        return stack
    def dfsright(root,stack):
        
        if not root:
            stack.append(None)
            return stack
        else:
            stack.append(root.value)
            dfsright(root.right,stack)
            dfsright(root.left,stack)
        return stack
    dfsleft(t,stackleft)
    dfsright(t,stackright)
    
    return stackleft == stackright