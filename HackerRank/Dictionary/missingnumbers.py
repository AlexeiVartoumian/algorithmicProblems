"""
Given two arrays of integers, find which elements in the second array are missing from the first array.

Example


The  array is the orginal list. The numbers missing are .

Notes

If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both lists is the same. If that is not the case, then it is also a missing number.
Return the missing numbers sorted ascending.
Only include a missing number once, even if it is missing multiple times.
The difference between the maximum and minimum numbers in the original list is less than or equal to .
Function Description

Complete the missingNumbers function in the editor below. It should return a sorted array of missing numbers.

missingNumbers has the following parameter(s):

int arr[n]: the array with missing numbers
int brr[m]: the original array of numbers
Returns

int[]: an array of integers
Input Format

There will be four lines of input:

 - the size of the first list, 
The next line contains  space-separated integers 
 - the size of the second list, 
The next line contains  space-separated integers 

Constraints

Sample Input

10
203 204 205 206 207 208 203 204 205 206
13
203 204 204 205 206 207 205 208 203 206 205 206 204
Sample Output

204 205 206
Explanation

 is present in both arrays. Its frequency in  is , while its frequency in  is . Similarly,  and  occur twice in , but three times in . The rest of the numbers have the same frequencies in both lists.
"""
  #this is a two dict problem 
    #algo goes as follows for count keep number as key freq as value
    #for all occuring numbers include in set
    #pop the set numbers one by one
    #case 1 number is in brr but not arr then append
    #case 2 number is in both but brr has more, append
    #when done sort the result


from collections import defaultdict
def missingNumbers(arr, brr):
    # Write your code here
  
    
    original = defaultdict(int)
    diff = defaultdict(int)
    length = len(arr) 
    allnums = set()
    for i in range(length):
        original[brr[i]] +=1
        diff[arr[i]]+=1
        allnums.add(brr[i])
        allnums.add(arr[i])
    for i in range(length,len(brr)):
        original[brr[i]] +=1
        allnums.add(brr[i])
    
    result = []
    
    while allnums:
        curnum = allnums.pop()
        if curnum in original and curnum in diff:
            if original[curnum] > diff[curnum]:
                result.append(curnum)
        elif curnum in original and curnum not in diff:
            result.append(curnum)
            
    result.sort()
    return result