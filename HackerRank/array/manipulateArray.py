"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example


Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below.

arrayManipulation has the following parameters:

int n - the number of elements in the array
int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Returns

int - the maximum value in the resultant array
Input Format

The first line contains two space-separated integers n and m 
the size of the array and the number of operations.
Each of the next m lines contains three space-separated integers a , b, k he left index, right index and summand.

Constraints
3 <=n <= 10 ^ 7
1 <= m <=2 * 10^5
1<= a <b <= n
0<= k<= 10 ^9
5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update the list is 100 100 0 0 0.
After the second update list is 100 200 100 100 100.
After the third update list is 100 200 200 200 100.

The maximum value is 200.
"""

"""
I tried to think about intersections and only consider intervals at frist . I then considered using sets to keep track of the bounds somehow and finally compute  the maximum sum. turns out that was leaning in towards the optimal solution. in the end I brute forced it but this is problem can actually be solved with a prefix sum but the intuition compeletely escaped me on that one. the approach is to increment the lowerbound by the k value but to decrement the higher bound value. in this fashion you can keep track of all the ranges that are in between two given bounds without having an ever increasing sum as you iterate over the array. bloody clever those prefix sums.
"""

def arrayManipulation(n, queries):
    # Write your code here
    starting = [0] * (n+1) # handle user input starting at 1
    
    for i in queries:
        lowbound,highbound, value = i
        starting[lowbound-1] += value
        starting[highbound] -= value
    
    maximum = 0
    runningsum =0
    
    for i in starting:
        runningsum+= i
        maximum = max(maximum,runningsum)
    
    return maximum




n = 10
queries = [[2, 6 ,8],[3 ,5 ,7],[1 ,8, 1],[5 ,9 ,15]]

def manipulate(queries,n):
    
    starting = [0] * n
    def maparray(arr1,arr2):
        
        res = [0] * len(arr1)
        for i in range(len(arr1)):
            res[i]= arr1[i] + arr2[i]
        return res
    for i in range(len(queries)):
        index1 = queries[i][0]
        index2 = queries[i][1]
        value = queries[i][2]
        addto = [value] * (index2 - (index1-1))
        prev = starting[index1-1:index2]
        starting = starting[:index1-1:] + maparray(prev,addto)+ starting[index2::]
    
    
    return max(starting)