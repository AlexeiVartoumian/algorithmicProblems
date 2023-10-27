"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""




"""
ARRRGRHHHHh!!!! insert swear word of PRIME choice and I DOO mean PRIMMME!! this problem took me on some lord of the rings journey
and my approach was all wrong to compute kadanes algo from most likely positions. the intuition of using prefix sums and suffix sums eluded me like that mgaical ghost from mario boo only this time im trying to catch the ghost and its running away and the natural language description of it took me longer than i like to admit to implement. oh well thats just the way it goes good days and bad. below is my final solution and the one below it is  godzillas nightmare which is basically incorrect handles 109/111 test cases but is still wrong.
nums =[5,-3,5]
#nums = [5,2,-3,-4,-5,7,-2,8,9]
#nums =[5,5,0,-5,3,-3,2]
#nums =[1,-2,3,-2]
#nums =[-1,-3,-25]
#nums = [-5,-2,5,6,-2,-7,0,2,8] 

"""

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        suffix = [0]* len(nums)
        suffix[-1] = nums[-1]
        suffixsum = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            suffixsum+= nums[i]
            suffix[i] = max(suffixsum,suffix[i+1])
    
        prefix =0
        special = nums[0]
        maximum = nums[0]
        maxsofar = 0
        for i in range(len(nums)):
            prefix+=nums[i]
            maxsofar = max(0,maxsofar) + nums[i]
            maximum = max(maxsofar,maximum)
            if i+1 < len(nums)-1:
            
                special = max(special,prefix+suffix[i+1])
        return max(maximum,special)


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def looping(start,step,length):
            count =0 
            maxsofar = 0
            maxsum =  0
            if step ==1:
                while count < length:
                    if maxsofar +nums[start % length] <0:
                        maxsofar =0
                    else:
                        maxsofar+=nums[start%length]
                        maxsum = max(maxsum,maxsofar)
                    count+=1
                    start+=1
                return maxsum
            else:
                while count < length:
                    if start == -1:
                        start = length-1
                    if maxsofar +nums[start % length] <0:
                        maxsofar =0
                    else:
                        maxsofar+=nums[start%length]
                        maxsum = max(maxsum,maxsofar)
                    count+=1
                    start-=1
                return maxsum
        negsonly = True
        maxsofar = 0
        maxsum = float("inf") * -1
        index = 0
        for i in range(len(nums)):
            if negsonly:
                if nums[i]>= 0:
                    maxsum = nums[i]
                    negsonly= False
                    maxsofar = nums[i]
                else:
                    maxsum = max(maxsum,nums[i])
            else:
                if maxsofar+nums[i] <=0:
                    maxsofar = 0
                else:
                    maxsofar+=nums[i]
                    if maxsofar >= maxsum:
                        maxsum =maxsofar
                        index = i
        if negsonly:
            return maxsum
        maxsofar = 0
        maxbacksum = float("inf") * -1
        negindex = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if negsonly:
                if nums[i]>= 0:
                    maxsum = nums[i]
                    negsonly= False
                    maxsofar = nums[i]
                else:
                    maxsum = max(maxbacksum,nums[i])
            else:
                if maxsofar+nums[i] <=0:
                    maxsofar = 0
                else:
                    maxsofar+=nums[i]
                    if maxsofar >= maxbacksum:
                        maxbacksum =maxsofar
                        negindex = i
    
    
        maxforward = looping(index,1,len(nums))
        maxbackward = looping(index,-1,len(nums))
        maxnegforward = looping(negindex,1,len(nums))
        maxnegbackward = looping(negindex,-1,len(nums))
        
        return max(maxsum,maxforward,maxbackward,maxnegforward,maxnegbackward)
