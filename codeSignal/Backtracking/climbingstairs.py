"""
You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.
"""
"""
Example

For n = 4 and k = 2, the output should be

solution(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.
"""
"""
now there is a dynammic programming solution to this answer where you store the number of ways to get from n-1 to n+1 and loop backwards to get the final answer. the above is essentially the cached version of the below. however since we are asked to return the array for combinations then the approach is to find all permutations that are equal n.
"""

def climbingstairs(n,k):

    if n == 0 or k == 0:
        return [[]] # impossible to make a move in either case
    res = []

    def backtrack(combo):
        
        if sum(combo) == n:
            res.append(combo.copy()) # append copy to account for not losing current combination in function calls
            return
        elif sum(combo) > n:
            return  # this decision tree route is busted

        else:
            for i in range(1,k+1):
                combo.append(i)
                backtrack(combo)
                combo.pop() # prune all explored options
        
    backtrack([])
    return res

