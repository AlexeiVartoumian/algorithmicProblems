"""
Andy wants to play a game with his little brother, Bob. The game starts with an array of distinct integers and the rules are as follows:

Bob always plays first.
In a single move, a player chooses the maximum element in the array. He removes it and all elements to its right. For example, if the starting array , then it becomes  after removing .
The two players alternate turns.
The last player who can make a move wins.
Andy and Bob play  games. Given the initial array for each game, find and print the name of the winner on a new line. If Andy wins, print ANDY; if Bob wins, print BOB.

To continue the example above, in the next move Andy will remove . Bob will then remove  and win because there are no more integers to remove.

Function Description

Complete the gamingArray function in the editor below.

gamingArray has the following parameter(s):

int arr[n]: an array of integers
Returns
- string: either ANDY or BOB

Input Format

The first line contains a single integer , the number of games.

Each of the next  pairs of lines is as follows:

The first line contains a single integer, , the number of elements in .
The second line contains  distinct space-separated integers  where .
Constraints

Array  contains  distinct integers.
For  of the maximum score:

The sum of  over all games does not exceed .
For  of the maximum score:

The sum of  over all games does not exceed .
"""

"""
the brute force approach will be to compute the maximum index at every turn and slice the array according to that index.
keep doing until array empty. but there is a better waw. according  to the rules of the game bob starts first and andy second. suppose arrray 1,2,3,4 or any array for that matter. if the number of operations to get to to empty array is even. then andy will have to win otherwise bob will win. therefore just keep track of the number of times the maxcount seen so far has been incremented when iterating through the array as that will be the number of the operations to get to zero.
"""

def gamingArray(arr):
    # Write your code here
    
    
    maxsofar = -1
    count = 0
    
    for i in arr:
        if i > maxsofar:
            maxsofar = i
            count +=1
    if count % 2 == 0:
        return "ANDY"
    return "BOB"