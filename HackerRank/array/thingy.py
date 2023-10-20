"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times the client will receive a notification over all  days.

Example


On the first three days, they just collect spending data. At day , trailing expenditures are . The median is  and the day's expenditure is . Because , there will be a notice. The next day, trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below.

activityNotifications has the following parameter(s):

int expenditure[n]: daily expenditures
int d: the lookback days for median spending
Returns

int: the number of notices sent
Input Format

The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending respectively.
The second line contains  space-separated non-negative integers where each integer  denotes .

Constraints

Output Format

Sample Input 0

STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
Sample Output 0

2
Explanation 0

Determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .

On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .

On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .

Sample Input 1

5 4
1 2 3 4 4
Sample Output 1

0
There are  days of data required so the first day a notice might go out is day . Our trailing expenditures are  with a median of  The client spends  which is less than  so no notification is sent.
"""





#arr = list(map(int,string.split(" "))) =>  turn hackerank testcase into a array
"""
the general appraocf for this problem was to  sort only once the window of 0 up to d indexes and find the median.
afterwhich keep track of incoming and outgoing values using a sliding window approach. for each of those values use binary search for deletion and binary search for insertion. However my hand coded version of those bin searches did not pass the timeout test even though the correct output. however the in built bisect function handled this that issue.
the inbuilt bisect function
""" 

import bisect
def activityNotifications(expenditure, d):
    # Write your code here
    """
my algorirthm is to use dict to store all indexes of values between
i and n. then compute median. then check the number directly ahead if d
is less than n. if irregular add to res. then remove last day using 
sliding
window technique and add the new number to the sorted list with binary 
search.
"""
    def calculatemedian(arr,median,d):
        if d % 2 == 0:
            median =(arr[len(arr)//2 - 1] +arr[(len(arr)//2)])/2
        else:
            median = arr[len(arr)//2]
        return median
    indexes={}
    indexcount=0 
    window=[]
    trailing=True
    result=0
    median=0
    def bin(arr, value):
        low = 0
        high = len(arr) - 1

        if value == arr[high]:
            return arr[:high]

        if value <= arr[low]:
            return arr[1:]

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == value:
                arr = arr[:mid] + arr[mid+1:]
                return arr
            elif arr[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
    def binarysearch(arr, value):
        low = 0
        high = len(arr)-1
        if value >= arr[high]:
            arr.append(value)
            return arr
        if value <= arr[low]:
            newarr = [value] + arr
            return newarr
        while low <= high:
            mid = (low + high) //2
            if arr[mid] == value:
                newarr = arr[:mid+1:] + [value] + arr[mid+1::]
                return newarr
            if arr[mid] > value and arr[mid-1] < value:
                newarr =  arr[:mid:] + [value] + arr[mid::]
                return newarr
            if arr[mid] < value and arr[mid+1] > value:
                newarr = arr[:mid+1:] + [value] + arr[mid+1::]
                return newarr
            if arr[mid] > value:
                high =mid-1
            else:
                low = mid + 1
    for i in range(len(expenditure)):
        if trailing:
            indexes[i] = expenditure[i]
            if i == d-1:
                trailing = False
                window = expenditure[:i+1:]
                window.sort()
                median = calculatemedian(window,median,d)
        else:
            if expenditure[i] >= median*2:
                result+=1
            #window = bin(window,indexes[indexcount])
            #del(indexes[indexcount])
            #indexcount+=1
            window.pop(bisect.bisect_left(window, expenditure[i-d]))
            bisect.insort_right(window, expenditure[i])
            #window = binarysearch(window,expenditure[i])
            #indexes[i] = expenditure[i]
            median = calculatemedian(window,median,d)
    return result


def activityNotifications(expenditure, d):
    # Write your code here


    def calculatemedian(arr,median,d):
        if d % 2 == 0:
            median =(arr[len(arr)//2 - 1] +arr[(len(arr)//2)])/2
        else:
            median = arr[len(arr)//2]
        return median
    indexes={}
    indexcount=0 
    window=[]
    trailing=True
    result=0
    median=0

    def bin(arr, value):
        low = 0
        high = len(arr) - 1

        if value == arr[high]:
            return arr[:high]

        if value <= arr[low]:
            return arr[1:]

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == value:
                arr = arr[:mid] + arr[mid+1:]
                return arr
            elif arr[mid] > value:
                high = mid - 1
            else:
                low = mid + 1
    def binarysearch(arr, value):
        low = 0
        high = len(arr)-1
        if value >= arr[high]:
            arr.append(value)
            return arr
        if value <= arr[low]:
            newarr = [value] + arr
            return newarr
        while low <= high:
            mid = (low + high) //2
            if arr[mid] == value:
                newarr = arr[:mid+1:] + [value] + arr[mid+1::]
                return newarr
            if arr[mid] > value and arr[mid-1] < value:
                newarr =  arr[:mid:] + [value] + arr[mid::]
                return newarr
            if arr[mid] < value and arr[mid+1] > value:
                newarr = arr[:mid+1:] + [value] + arr[mid+1::]
                return newarr
            if arr[mid] > value:
                high =mid-1
            else:
                low = mid + 1
    for i in range(len(expenditure)):
        if trailing:
            indexes[i] = expenditure[i]
            if i == d-1:
                trailing = False
                window = expenditure[:i+1:]
                window.sort()
                median = calculatemedian(window,median,d)
        else:
            if expenditure[i] >= median*2:
                result+=1
            #print("final bincount = ", bincount)
            window = bin(window,indexes[indexcount])
            del(indexes[indexcount])
            indexcount+=1
            window = binarysearch(window,expenditure[i])
            indexes[i] = expenditure[i]
            median = calculatemedian(window,median,d)
    
    return result


#activityNotifications(arr,9999)