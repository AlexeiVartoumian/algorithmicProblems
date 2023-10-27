"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""
"""
could have gone for a while loop but i approached it by taking the first element- making that into the first interval as in [i,i] and then after than comparing every consequent element with interval[-1] updating it if its ahead by one. handle instance where its just one interval or the last interval is of greater value than the last in intevals and then genreate string sequence according.
"""
def summaryRanges( nums) :

        if not nums:
            return []
        intervals = []
        
        temp = [nums[0],nums[0]]

        results = []
        for i in range(1,len(nums)):

            if nums[i] == temp[-1]+1:
                temp[-1] = nums[i]
            else:
                intervals.append(temp)
                temp = [nums[i],nums[i]]
        
        if not intervals:
            intervals.append(temp)
        elif temp[-1] > intervals[-1][-1]:
            intervals.append(temp)
        
        for i in intervals:
            
            if i[0] == i[1]:
                thing = str(i[0])
                results.append(thing)
            else:
                thing = f'{i[0]}->{i[1]}'
                results.append(thing)
        return results