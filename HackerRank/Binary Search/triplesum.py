
"""
Given  arrays  of different sizes, find the number of distinct triplets  where  is an element of , written as , , and , satisfying the criteria: .

For example, given  and , we find four distinct triplets: .

Function Description

Complete the triplets function in the editor below. It must return the number of distinct triplets that can be formed from the given arrays.

triplets has the following parameter(s):

a, b, c: three arrays of integers .
Input Format

The first line contains  integers , the sizes of the three arrays.
The next  lines contain space-separated integers numbering  respectively.

Constraints



Output Format

Print an integer representing the number of distinct triplets.

Sample Input 0

3 2 3
1 3 5
2 3
1 2 3
Sample Output 0

8 
Explanation 0

The special triplets are  .

Sample Input 1

3 3 3
1 4 5
2 3 3
1 2 3
Sample Output 1

5 
Explanation 1

The special triplets are 

Sample Input 2

4 3 4
1 3 5 7
5 7 9
7 9 11 13
Sample Output 2

12
Explanation 2

The special triplets are
"""
"""
this is a bianry search problem where the idea is to remove duplicates and then therefter find the position of the first integer such that satisfirs the condition p <= q and q >= r. thought I could implemnent with three pointers but it  was not time efficient.
"""



# Use binary search to find where q is, or should be in the array
def binary_search(arr, target):
        high, low = len(arr) - 1, 0
        mid = (high + low) // 2
        sample = arr[mid]
        l_arr = len(arr)
        while low <= high:
            if target < sample:
                high = mid - 1
            elif target > sample:
                low = mid + 1
            else:
                # Add 1 since we want count of elements q is >=
                return mid + 1
            
            mid = (high + low ) // 2
            sample = arr[mid]
        
        # Add 1 since we want count of elements q is >=
        return high + 1  # Will be 0 or len(arr)
    
        a, b, c = list(set(a)), list(set(b)), list(set(c))
        a.sort()
        b.sort()
        c.sort()

        a_len, c_len = len(a), len(c)
        max_pr = product = result = 0
        for q in b:
            if max_pr:
                result += max_pr
            else:   
                p = binary_search(a, q)
                r = binary_search(c, q)
                if p and r:
                    product = p * r
                    if p == a_len and r == c_len:
                    # Once q is > all elements in p and r, simply resuse
                    # this max product.
                        max_pr = product

                    result += product
    
        return result

def triplessum(a,b,c):
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    a.sort()
    b.sort()
    c.sort()
    left = 0
    right = 0
    final = 0
    groups = []
    while left < len(a):
        combo = []
        combo.append(a[left])
        while right < len(b) and  b[right] < a[left]:
            right+=1
        if right < len(b) and b[right] >= a[left]:
                for j in range(right, len(b)):    
                    temp = combo.copy()
                    temp.append(b[j])
                    while final < len(c) and c[final] > b[j]:
                        final+=1
                    if final < len(c) and c[final] <=b[j]:
                        for i in range(final, len(c)):
                            combination = temp.copy()
                            if c[i] <= temp[-1]: 
                                combination.append(c[i])
                                groups.append(combination)
                            else:
                                break
                    final = 0
        left+=1
        right = 0
        final = 0
    return len(groups)            