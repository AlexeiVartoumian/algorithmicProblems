"""
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.
"""
"""
solved this problem yesterday with backtracking, although the problem statement asked for all permutations which is why the constraints for that one was up to 10. as such the right question to ask here is suppose you are on step 4 of 5 , how many ways are there to get to step 4 to 5. there is one. and the same again for three to five. there are two. all subsequent ways from two to five and 1 to five will be the sum of the last two counts a fibonacci sequence. maintain a record of length n where the last two elements are filled 1 and 2. then loop to zero applying fib. return first record which will be the number of ways to step from 0 to n with either 1 or two steps.
"""


def climbingstairs(n):

    if n < 3:
        return n
    records = [0] * n

    records[-1] = 1
    records[-2] = 2

    for i in range(len(records)-3,-1,-1):
        records[i] = records[i+1] + records[i+2]

    return records[0] 