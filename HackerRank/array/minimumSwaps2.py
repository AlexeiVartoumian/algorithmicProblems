"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

Example


Perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below.

minimumSwaps has the following parameter(s):

int arr[n]: an unordered array of integers
Returns

int: the minimum number of swaps to sort the array
Input Format

The first line contains an integer, , the size of .
The second line contains  space-separated integers .

Constraints

Sample Input 0

4
4 3 1 2
Sample Output 0

3
Explanation 0

Given array 
After swapping  we get 
After swapping  we get 
After swapping  we get 
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 1

5
2 3 4 1 5
Sample Output 1

3
Explanation 1

Given array 
After swapping  we get 
After swapping  we get 
After swapping  we get 
So, we need a minimum of  swaps to sort the array in ascending order.

Sample Input 2

7
1 3 5 2 4 6 7
Sample Output 2

3
"""

"""
the first thing to observe here is that all elements are between 1 and length of array which means
that we can take advantage of this property by saying this. for each element in the list store its current index
say 1 is at position 0 then it does not need to be swapped. once this has been done the idea thereafter is that for every element 
that does not equal index +1 since we start at 1 find out where i+1 currently is and swap the two elements updating the dictionary
everytime. do this every time current element is not equal to i+1 .
eg : 1,4,3,2 on first pass nothing happens. then 4 != i +1 where i is now 1 . therefore find i+1 in table where its value stored as index is 3. we can now swap the two and increment count array is now 1,2,3,4 . update the hashtable for both values
"""


arr = [1, 7, 3, 2, 4, 5, 6]

def minimumswaps(arr):
    
    indexmap = {}
    for i in range(len(arr)):
        indexmap[arr[i]] = i
    count =0 
    for i in range(len(arr)):
        if arr[i] != i + 1:
            currentvalue = arr[i] # grab current value to update hashtable
            tempindex = indexmap[i + 1] # find where needed value is
            arr[i], arr[tempindex] = arr[tempindex], arr[i] # swap the the current value to its temp index
            indexmap[currentvalue] = tempindex # update current value to 
            indexmap[i + 1] = i # i+1 is now in its correct position
            count += 1
    return count

minimumswaps(arr)