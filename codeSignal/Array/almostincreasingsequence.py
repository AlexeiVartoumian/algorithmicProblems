"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

sequence: [1, 3, 2, 1] Expected return value false
sequence: [1, 2, 1, 2] Expected return value false
sequence: [3, 6, 5, 8, 10, 20, 15] Expected return value false
sequence: [10, 1, 2, 3, 4, 5] Expected return value true
"""

"""
this is a conditional flow logic problem. imagine a sequence of numbers and the goal is to determine where the outlier is. in the case where the numbers are strictly ascending then continue. the first case where an outlier has been found is when the  current number is smaller than the previous largest seen number i.e 10,11,9,13 . in which case add 1 to the number of removals required when 9 is seen. but what about the case where the outlier is a previously seen number?
 consider the array sequence: [10, 1, 2, 3, 4, 5] . the simple case would be to say that since 1 is smaller than 10 add 1 to removals. however we should look at the given array as if it was part of a continous sequence. as such set to variables to negative infinity. on the first pass if sequence[i] > then curmax all is well. here update curmax to 10 and prevmax to curmax prev value which was neg inf.
 on the second pass i is smaller then current max. its here where we can determine if the previous number is an outlier. if sequence[i] > curmax failed and seqeunce[i] > prevmax is true
 where prevmax is neg inf then we are saying we have a number larger than the current sequence of increasing numbers and it must be removed and here it is 10. therefore add 1 to removals and set the current maximum to 1.
 if number of removals is greater than 1 return False
"""

def solution(sequence):
    
    removals = 0
    
    
    prevmax,curmax = float("-inf"), float("-inf")
    for i in range(len(sequence)):
        print(sequence[i],prevmax,curmax)
        if sequence[i]> curmax:
            
            prevmax = curmax
            curmax = sequence[i]
        
        elif sequence[i] > prevmax:
            removals+=1
            curmax = sequence[i]
        else:
            removals+=1

    return removals <2