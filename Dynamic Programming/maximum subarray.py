
alist = [1,-1,1]


"""
revisited a few months later
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curmax = nums[0]
        runningsum= nums[0]
        if runningsum < 0:
            runningsum = 0
        
        for i in range(1,len(nums)):
            runningsum+= nums[i]
            curmax = max(curmax,runningsum)

            if runningsum <0:
                runningsum = 0
        return curmax



#myimplementation of the correct answer
def maxSubArray( nums):

        maxnow = nums[0]
        """
        the key to this algorithm is the variable maxnowplusend below. because we are only interested with continuos segments of subarrays and
        thier respective maximum values the variable maxnowplusend acts as a cumalative sum tracker. this will be contantly checked with the
        maxnow variable to see which is larger. this handles the case where all elements in the array are positive. howver 
        in the instance where there are negative elements in the array as well we will reset the maxstart variable to zero.
        this will handle the instance of when there is a continuos sequence of negative and positive elements. 
        
        if maxnowplusend ever falls below 
        zero then that means the continuos elements in that larger subarray has a smaller sum value than a smaller subarray sum value contained within the larger subarray. In this sense the variable works like a sliding window. two more things need to be done at every iteration
        maxnowplusend must be checked with the maxnow variable to see which is the larger value and maxnow must be updated to maxnowtillend if the
        latter is larger. it is important that if maxnowtill end is smaller than zero to first set it to zero and then add the current value
        to handle the instance where the the current element is positive but maxnowplus end is a a large negative value and maxnow is also a negative value.

        finally the case must be handled where all the integers in the array are negative. without any checks theabove sequence of steps will return zero since if maxendtillnow ever falls below zero it is set to zero and that is compared with maxnow. to handle this a boolean tracker is kept in place that checks the first value is negative or positive. if its negative it will remain true and a negative largest value will be updated to single negative variables ( the largest being -1) and that will be returned . if a element is positive than the boolean is set to false and maxnow is set to that value.
        """
        maxnowplusend = nums[0] 
        negativetrack = None
        neglargest =None
        if maxnow <0:
            negativetrack = True
            neglargest = nums[0]
        else:
            negativetrack = False
        for i in range(1, len(nums)):
        
            if negativetrack:
                if nums[i] > 0:
                    negativetrack = False
                else:
                    if nums[i] > neglargest:
                        neglargest = nums[i]
        
            
            if maxnowplusend <0:
                maxnowplusend = 0
            maxnowplusend += nums[i]
            if maxnowplusend > maxnow:
                maxnow = maxnowplusend
            maxnow = max(maxnow,nums[i])
    
        if negativetrack:
            return neglargest
        return maxnow
"""
#wrong answer below
def maximumsubarray(nums):
        if len(nums) == 2:
            if nums[0] < 0 and nums[1] < 0:
                return max(nums)
            elif nums[0] < 0:
                return nums[1]
            elif nums[1]<0:
                return nums[0]   
        haha = [0] * len(nums)
        cursum = nums[0]
        haha[0] = cursum
        start = 0
        temp = None
        end = None
        tempmax = cursum
    
        curmax = cursum
        for i in range(1,len(nums)):
        
            cursum+= nums[i]
            haha[i] = cursum
        
            if cursum > haha[start] and cursum < 0 or cursum < haha[start] and nums[i] > curmax or cursum < 0 and nums[i]==0:
                start = i
                curmax = nums[i]
                temp = nums[i]
                tempmax = nums[i]
            elif cursum > haha[start] and cursum >=0:
                if temp != None:
                    if temp < 0:
                    
                        if end != None:
                            if curmax + temp + haha[i] > curmax:
                                end = i
                            else:
                                continue
                        else:
                            start = i
                            temp = nums[i]
                        if nums[i] > curmax:
                            tempmax = nums[i]
                            curmax = nums[i]
                    else:
                    
                        tempmax += nums[i]
                        end = i
                else:
                    temp = nums[i]
                    tempmax+=nums[i]
            elif cursum > 0:
                tempmax+= cursum
            else:
                if temp != None:
                    temp+=nums[i]
                    tempmax +=nums[i]
                else:
                    tempmax += nums[i]
        
            if tempmax > curmax:
                curmax = tempmax
        
        return curmax


print(maximumsubarray(alist))
"""