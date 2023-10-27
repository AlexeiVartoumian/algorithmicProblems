"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

"""
I approached this with binary search but its way to inefficient with many checks my search works by checking every array including high 
--- while low<= high and incrementing low to mid +1 . after that there are three cases to take care of
case1: target value is smaller or equal to first value in array and larger or equal to value in array. that means do binary seach in that array 
case2: low, mid and high all equal each other: to avoid infinite loop check if target is in this array if it is perform binary search. if not return false
case3: the element is not in the array then low bound is either equal to high or has surpassedit

again there is too much processing here. a more optimal solution here is to the code below it which also performs bianry search. it avoids the complexity of nested 2d arrays entirely by treating the matrix as a 1 dimensional array. it does this by accessing the row with the operation
row = mid// n and column = mid % n where n is the length of nested array inside the matrix. at that point its just a simplified binary search.

AN elegeant solution is the last one that takes advantage of the nature of the matrix and the question. it simply uses a for loop to check the last element of every array and then since we dont have to return an index only true or false returns target in given array.
"""
def searchMatrix( matrix, target) :
        low = 0
        high = len(matrix)-1
    
        while low <=high :
        
            mid = int((low + high)/2)
            if low == mid and high == mid:
                if  target >=matrix[mid][0] and target<= matrix[mid][-1]:
                    if target == matrix[mid][0] or target == matrix[mid][-1]:
                        return True
                
                    low = 0
                    high = len(matrix[mid])-1
                    i = mid
                    while low < high:
                        mid = int((low + high)/2)
                        if target == matrix[i][mid]:
                            return True
                        if target > matrix[i][mid]:
                            low = mid +1
                        else:
                            high = mid
                    return False
            
                return False
            if  target >=matrix[mid][0] and target<= matrix[mid][-1]:
                if target == matrix[mid][0] or target == matrix[mid][-1]:
                    return True
                low = 0
                high = len(matrix[mid])-1
                i = mid
                while low < high:
                    mid = int((low + high)/2)
                    if target == matrix[i][mid]:
                        return True
                    if target > matrix[i][mid]:
                        low = mid +1
                    else:
                        high = mid
                return False
                
                
        
        
            if target > matrix[mid][0]:
                low = mid +1
            else:
                high = mid 
        return False

def searchMatrix1( matrix, target) :
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1 # number of elements in array 

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            num = matrix[row][col]

            if num == target:
                return True

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
def searchMatrix2(matrix, target): 
        for i in matrix:
            if i[-1] >= target:
                return target in i
        return False