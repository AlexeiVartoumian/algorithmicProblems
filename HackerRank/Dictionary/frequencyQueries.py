"""
You are given  queries. Each query is of the form two integers described below:
-  : Insert x in your data structure.
-  : Delete one occurence of y from your data structure, if present.
-  : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

Example

The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1
Return an array with the output: .

Function Description

Complete the freqQuery function in the editor below.

freqQuery has the following parameter(s):

int queries[q][2]: a 2-d array of integers
Returns
- int[]: the results of queries of type 

Input Format

The first line contains of an integer , the number of queries.
Each of the next  lines contains two space-separated integers,  and .

Constraints

All 
Sample Input 0

8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2
Sample Output 0

0
1
Explanation 0

For the first query of type , there is no integer whose frequency is  (). So answer is .
For the second query of type , there are two integers in  whose frequency is  (integers =  and ). So, the answer is .

Sample Input 1

4
3 4
2 1003
1 16
3 1
Sample Output 1

0
1
Explanation 1

For the first query of type , there is no integer of frequency . The answer is . For the second query of type , there is one integer,  of frequency  so the answer is .

Sample Input 2

10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2
Sample Output 2

0
1
1
Explanation 2

When the first output query is run, the array is empty. We insert two 's and two 's before the second output query,  so there are two instances of elements occurring twice. We delete a  and run the same query. Now only the instances of  satisfy the query.
"""

"""
initially failed the test cases because I omiited to consider that I need to first Remember the current frequency of 
a given number whenever 1 or two occurs keeping account for the fact that if a numbers frequency goe sup by 1 to 2 , then its frequency is no longer 1 and that therefore the frequency of that frequency now needs to be decremented.
"""
from collections import defaultdict
def freqQuery(queries):
    
    freqCounts = defaultdict(int) # where int is the frequencies of frequencies
    # the key  is the frequency the value is the number
    frequencies= defaultdict(int) # where int is the frequency of number to be recorded
    answers = []
    cur = 0
    for order,number in queries:
       
        if order == 1:
            # Increase the frequency of 'number'
            prev_freq = frequencies[number]
            frequencies[number] += 1
            freqCounts[prev_freq] -= 1
            freqCounts[frequencies[number]] += 1
        elif order == 2:
            if frequencies[number] > 0:
                # Decrease the frequency of 'number' if it's greater than 0
                prev_freq = frequencies[number]
                frequencies[number] -= 1
                freqCounts[prev_freq] -= 1
                freqCounts[frequencies[number]] += 1
        elif order == 3:
            if number in freqCounts and freqCounts[number] > 0:
                answers.append(1)
            else:
                answers.append(0)
    return answers
