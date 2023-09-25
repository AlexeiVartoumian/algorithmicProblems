"""
You are planning to rob houses on a specific street, and you know that every house on the street has a certain amount of money hidden. The only thing stopping you from robbing all of them in one night is that adjacent houses on the street have a connected security system. The system will automatically trigger an alarm if two adjacent houses are broken into on the same night.

Given a list of non-negative integers nums representing the amount of money hidden in each house, determine the maximum amount of money you can rob in one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
solution(nums) = 2.

The optimal way to get the most money in one night is to rob the first and the third houses for a total of 2.
"""

"""
I've encountered this problem before but wanted to practise. as such the question I asked myself was how do I store alternate sums but at the same time be as greedy as possible ? consider a loop which moves in linear fashion it will inevtiably "alternate" from one element to the next. at each step store the current element in a vriable and greedily choose between cursum and prevsum + current iteration. because the nature of the loop is iterative in nature , use this as a way to alternate the sums and continue the above. return the greedy sum.
"""
def solution(nums):
    
    if not nums:
        return 0
    lilrob = 0
    bigrob = nums[0]
    
    for i in range(1,len(nums)):
        temp = bigrob
        bigrob =max(lilrob+nums[i],bigrob)
        lilrob = temp        
        
    
    return bigrob