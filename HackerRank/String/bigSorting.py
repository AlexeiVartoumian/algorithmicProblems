"""
Consider an array of numeric strings where each string is a positive number with anywhere from 1 to 10^6  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and return the sorted array.

example:
unsorted = ["1","200",'150',"3"]
Return the array ['1', '3', '150', '200'].

Function Description

Complete the bigSorting function in the editor below.

bigSorting has the following parameter(s):

string unsorted[n]: an unsorted array of integers as strings
Returns

string[n]: the array sorted in numerical order
Input Format

The first line contains an integer, n, the number of strings in unsorted.
Each of the n subsequent lines contains an integer string,unsorted[i] .
"""
"""
My first approach was to use a modification of binary search to insert the string rep of the numbers in sorted order.
My second approach was to use mergesort on the array of strings.
both work on principle but did not pass the tests as very large strings were being passed into the array.

the actual approach is to take advantage of the length of the strings. building on this clever clue first group the numbers according to theier length. then sort the numbers which are the keys. then for each of those groups sort them again adding it to  the subarray.
"""

from collections import defaultdict
def bigSorting(unsorted):
    # Write your code here
    buckets = defaultdict(list)
    
    for i in unsorted:
        number = len(i)
        buckets[number].append(i)
    res = []
    
    for i in sorted(buckets.keys()):
        res+= sorted(buckets[i])
    return res



def bisorting2(arr):
    def mergesort(arr):
        
        if len(arr) > 1:
            mid = len(arr)//2
            left  = arr[:mid:]
            right = arr[mid::]
            mergesort(left)
            mergesort(right)
            i = 0
            j = 0 
            k = 0
            while i < len(left) and j < len(right):
            
                if int(left[i]) < int(right[j]):
                    arr[k] = left[i]
                    i+=1
                    k+=1
                elif int(left[i]) > int(right[j]):
                    arr[k] = right[j]
                    k+=1
                    j+=1
                elif int(left[i]) == int(right[j]):
                    arr[k] = left[i]
                    arr[k+1] = right[j]
                    i+=1
                    j+=1
                    k+=2
            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1
        return arr
    arr = mergesort(arr)
   
    return arr




     
# def bigSorting(unsorted):
#     # Write your code here
#     res = []
    
#     def binsearch(value, res):
        
#         if not res:
#             res.append(str(value))
#             return res
#         low = 0
#         high = len(res)-1
#         if value <= int(res[low]):
#             res = [str(value)] + res
#             return res
#         elif value >=int(res[high]):
#             res.append(str(value))
#             return res
        
#         while low <= high:
#             mid =int( (low+ high) /2)
#             if value== int(res[mid]) or (value <= int(res[mid]) and value > int(res[mid-1])):
#                 res = res[:mid:] + [str(value)] + res[mid::]
#                 return res
#             elif value >= int(res[mid]) and value < int(res[mid+1]):
#                 res = res[:mid+1:] + [str(value)] + res[mid+1::]
#                 return res
            
#             if int(res[mid]) > value:
#                 high = mid
#             else:
#                 low = mid 
                
#     for i in unsorted:
#         if i :
#             number = int(i)
#             res = binsearch(number,res)
    
    
    
#     return res