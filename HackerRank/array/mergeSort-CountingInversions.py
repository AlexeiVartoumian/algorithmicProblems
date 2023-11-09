"""
in an array arr , the elements at indices i and j (where i < j) form an inversion if arr[i] > arr[j]. in other words , inverted elements arr[i] and arr[j] are considered to be "out of order". to correct an inversion , we can swap adjacent elements

eg : arr[2,4,1]

to sort the array , we must perform the following two swaps to corret the inversions

the sort has two inversions (4,1) and (2,1).
given an array arr, return the number of inversions to sort the array.
"""

"""
The way I first understood this question was that i of course
will have to apply merge sort to an array of numbers with the condition that wheneever right[j] > left[i] then we have encountered an element greater than relative to position and therfore increment. the problem was that  i could not keep track of the nuber of times this happended correctly when merge sorting in place. as such the update was to apply merge sort but instead append the arrays to a left and right queue where I could now say whenever the right[0] element was > than left[0] then the number of swaps to be done at this part of the sortingt will be the length of the left queue.
"""

from collections import deque
def inversions(arr):

    def mergesort(arr,count):
        
        if len(arr) <=1:
            return arr,count
        result = []
        mid = len(arr)//2
        left , count = mergesort(arr[:mid:],count)
        left= deque(left)
        right,count = mergesort(arr[mid::],count)
        right = deque(right)

        while len(left) and len(right):

            if left[0] <= right[0]:
                result.append(left.popleft())
            else:
                result.append(right.popleft())
                count += len(left)
        result.extend(left)
        result.extend(right)
        
        return result, count
    return mergesort(arr,0)[1]

arr = [2,1,3,1,2]
print(inversions(arr))