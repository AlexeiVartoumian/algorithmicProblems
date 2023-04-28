"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
"""
the key to solving this questions is that you can return the result in any order. because the intial order of the array does not matter a simple appraich would be to just sort both arrays and have two pointers ; one that keeps track of the smaller array elements and the other for the larger for example
arr1 = [1,2,2,3,4]
arr2 = [4,3,2,3,3,1]
the intersection is [1,2,3,4] all that needs to be done is see if the element in the shorter array exists in the longer one and if so append it to the final result. below is using this idea but with  a dictionary
that does not sort each array but instead keeps track of the frequency of each element in the shorter array. then loop through the longer array and tally down the frequency.
"""
arr1 = [1,2,2,3,4]
arr2 = [4,3,2,3,3,1]
def intersect(nums1, nums2):

        theobject = {}
        res = []
        #determine which is the shorter array and make the object
        #that keeps tradk of frequency for that one
        if len(nums1)< len(nums2):

            for i in range(len(nums1)):
                if nums1[i] not in theobject:
                    theobject[nums1[i]] =1
                else:
                    theobject[nums1[i]]+=1
            
            for i in range(len(nums2)):
                if nums2[i] in theobject and theobject[nums2[i]]:
                    theobject[nums2[i]]-=1
                    res.append(nums2[i])
            return res
            
        else:
            for i in range(len(nums2)):
                if nums2[i] not in theobject:
                    theobject[nums2[i]] =1
                else:
                    theobject[nums2[i]]+=1
            
            for i in range(len(nums1)):
                if nums1[i] in theobject and theobject[nums1[i]]:
                    theobject[nums1[i]]-=1
                    res.append(nums1[i])
            return res

prices =[3,3,5,0,0,3,1,4]

def maxProfit(prices):

        if len(prices) == 1:
            return 0
        
        
        if prices[0] > prices[1]:
                lowest= prices[1]
                highest = prices[1]
                lowind = 1
                highind = 1
                seclow = prices[1]
                sechigh = prices[1]
                seclowind = 1
                sechighind = 1
        elif prices[1] >= prices[0]:
                lowest= prices[0]
                highest = prices[1]
                lowind = 0
                highind = 1

                seclow = prices[0]
                sechigh = prices[1]
                seclowind = 0
                sechighind = 1

        
        for i in range(2,len(prices)):

                if prices[i] > seclow and i > seclowind:
                    sechigh = prices[i]
                    sechighind = i
                elif prices[i] <= seclow:
                    seclow = prices[i]
                    seclowind = i

                if sechigh- seclow > highest-lowest and seclowind < sechighind:
                    highest = sechigh
                    lowest = seclow
                    lowind = seclowind
                    highind = sechighind
        
        if lowind >= highind:
            return 0
        
        return highest - lowest
print(maxProfit(prices))