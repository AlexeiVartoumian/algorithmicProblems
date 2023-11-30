"""
Chief's bot is playing an old DOS based game. There is a row of buildings of different heights arranged at each index along a number line. The bot starts at building 0 and at a height of 0. You must determine the minimum energy his bot needs at the start so that he can jump to the top of each building without his energy going below zero.

Units of height relate directly to units of energy. The bot's energy level is calculated as follows:

if the bot's botEnergy is less than the height of the building, his
newEnergy = botEnergy - (height - botenergy)

if the botEnergy is greater than the height of the building his 
newEnrgy = botEnergy + (botEnergy - height)

Example 
arr = [2,3,4,3,2]
starting with boteergy = 4, we get the following table: 
botEnergy   height  delta
    4               2       +2
    6               3       +3
    9               4       +5
    14              3       +11
    25              2       +23
    48
    That allows the bot to complete the course, but may not be the minimum starting value. The minimum starting botEnergy in this case is 3.
"""
"""
my first approach completely ignored the mathematical aspect of this problem
which is the elegant and efficient way to solve. as such I used binary search to find the minimum value. however looking at the formula 
Ne = Be - (h - Be)  when Be < h
Ne = Be + (Be - h) when Be > h

when expanded are exactly the same thing i.e
Ne = Be - (h - Be) => Be -h + Be => 2Be -h
Ne = Be + (Be - h) => Be + Be -h => 2Be -h

this could be applied iteratively from the start and repeated until minimum is found. However starting from the back of the array where we expect to have the finished result what if the reverse was applied? that is the formula (2Be-h) is reversed into (h+Be)/2 where Be is now the minimum energy required starting at zero and go backwards to the first element will reveal the minimum energy required. as such start with minimum being set to zero applying the reverse until first element.
"""
import math
def chiefHopper(arr):
    minimum = 0
    for i in (arr[::-1]):
        minimum = math.ceil((i + minimum)/2)
    return minimum

def chiefHopper(arr):
    # Write your code here
    double = 2
    prev = double
    def delta(E,height, greaterThan):
        if greaterThan:
            return height - E
        else:
            return E- height
    def ispossible(E):
        for i in range(len(arr)):
            if arr[i] > E:
                E -= delta(E,arr[i],True)
                if E <0:
                    return False
            elif arr[i] < E:
                E += delta(E,arr[i],False)
                if E< 0:
                    return False
        return True
    def binsearch(low,high):
        
        while low<=high :
            mid = int((low+high)/2)
            val = ispossible(mid)
            lowerval = ispossible(mid-1)
            if val and not lowerval:
               return mid
            
            if not val:
                low = mid+1
            else:
                high = mid
    notFound = True
    while notFound:
        if ispossible(double):
            return binsearch(prev,double)
        else:
            prev = double
            double*=2