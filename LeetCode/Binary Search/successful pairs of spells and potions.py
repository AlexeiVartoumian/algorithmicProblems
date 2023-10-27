
"""
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
"""
"""
first sort potions. then for every item of spells do a binary search on soreted potions. the potions[i] * spells[mid] < success but 
potions[i] * spells[mid+1] is greater or equal to success then the number of items gfor that combination will be len(array) - mid+1.
"""





def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        res = []
        def binarysearch(low,high,curval,arr):

            while low <= high:
                mid = int((low+high)/2)
                if curval*arr[mid] < success:
                    low = mid
                    if curval*arr[low+1] >= success and curval*arr[low] < success:
                        return len(arr) - (low+1)
                    while low <=high:
                        mid = int((low+high)/2)
                        if curval*arr[mid+1] >= success and curval*arr[mid] < success:
                            return len(arr) - (mid+1)
                        
                        if curval*arr[mid] >= success:
                            high = mid
                        elif curval* arr[mid] < success:
                            low = mid
                if curval*arr[mid] >=success:
                    high = mid
                else:
                    low = mid
        for i in range(len(spells)):

            if  spells[i] * potions[0] >= success:
                res.append(len(potions))
            elif spells[i] * potions[-1] < success:
                res.append(0)
            else:
                cur = 0
                cur = binarysearch(0,len(potions)-1,spells[i],potions)
                res.append(cur)
        return res