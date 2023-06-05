"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

[1,0,0,0]
[0,0,0,0,0,1]
[0]
"""
"""
I fell hard on this question. my intial approach was to simply count the zeroes as i traverse the array and for every second zero I mark it with a one. this is where I got a bunch of errors with the test cases above. instead of tracking the zeroes I should have tracked the space between the ones. as such the rule is for every three spaces there can exists two ones that are not adjacent to each other. as such I handled this by first marking the posititions of all the ones in the array. then handle all edge cases. if there are no ones then start from begining and mark every 2nd space after that with a one. if there is one 1 then have two pointers starting at two positions away respectively and move to the upper and lower bound of array marking a 1 as you go. finally if there are many ones in the array do the same go to lower bound for the lowest element and go to the highest bound for the highes element marking a one every two elements. then the trick of this question is then two get the difference between two elements. if there are four spaces in between them or three spaces you can only place one 1 in between them. if there are 5 spaces or 6 spaces then you can only place two 1's in between them. anything less than 3 does not count. as such the difference would be (i+1 - i )-1 to account for zero index and if that number is even then the number of ones that can be placed there are floor((n-1)/2) and for odd floor(n/2).
"""
import math
def canPlaceFlowers(flowerbed, n):
        if n == 0:
            return True
        onepositions = []

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                onepositions.append(i)
        
        vals = n
        if not onepositions:
            for i in range(0,len(flowerbed),2):
                vals-=1
                if vals<=0:
                    return True
            return vals <=0
        
        elif len(onepositions)==1:
            x = onepositions[0]-2
            j = onepositions[0]+2
            while x >= 0 :
                vals-=1
                x-=2
            while j <len(flowerbed):
                vals-=1
                j+=2
            return vals<=0
        else:
            x = onepositions[0]-2
            j = onepositions[-1]+2
            while x >= 0 :
                vals-=1
                x-=2
            while j <len(flowerbed):
                vals-=1
                j+=2
            if vals<=0:
                return True
            for i in range(len(onepositions)-1):
                diff = onepositions[i+1]- onepositions[i] -1

                if diff >=3:
                    if diff % 2 == 0:
                        vals-= math.floor((diff-1)/2)
                    else:
                        vals-= math.floor(diff/2)
            return vals<=0