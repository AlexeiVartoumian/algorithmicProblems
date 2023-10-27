"""
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0
"""

"""
the first thing to consider is how to determine the number of subarrays in a array oif length n. to do this we use two variables where the one is a growing sum and the other is the accumalation of that sum. consider an array of length 8 and two variables contiguous and result, where contiguous will keep track of the number of elements and result will be the accumalation of contiguos. as such the number of subarrays in an array of length 8 can re represented as follows:

contiguous = 0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 
result     = 0, 1 , 3 , 6 , 10, 15, 21, 28, 36
which is  (n * n+1)/2. 
at every step we calculate contiguous = contigous+1 and result = result + contiguous.
Once we know this its simply modifying the above to the contstraints of the problem.
constraint number1: we can only begin counting sub arrays when there is a sequence of length 3. 
constraint number 2: a sequence is only a sequence if the difference is the same.
to handle these constraints we start at the second element and define the current difference as current element minus previous element. ON THE THIRD ELEMENT, if it is equal to the difference then our contiguous sum increases and the number os subarrays incereasing according to the formula above. to handle different contiguous arithmetic slice sub arrays arrays appearing in the same array, if the above condition is not satisified then contigous is reset and the new difference is  current element minus previous element.
"""

def numberOfArithmeticSlices(nums):


        contiguous = 0
        result = 0

        currentdifference = None

        for i in range(1,len(nums)):

            if currentdifference is not None and  nums[i] -nums[i-1] == currentdifference:

                contiguous +=1
                result+= contiguous
            else:
                contiguous = 0
                currentdifference = nums[i] - nums[i-1]  
        
        return result