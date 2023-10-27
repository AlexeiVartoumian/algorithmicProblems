"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""
the way I approached this was to have an official index counter that subtracts the lower index from the higher index to obtain the profit and a secondary index pointers that keep track of 
all the following low and high values. if at any stage the secondary pointers has a greater value than the official lower and higher then set the official to those values and disregard everything to the left of the current index. 

however a much cleaner and elegant solution is the one directly below , that does the same thing but does not have two trackers. as the loop carries through it only cares about the current maximum and the current lowest. if at any point the current element subtracted by whatever the smallest element is , is a larger value than the current maximum then set maximum to that.
this works because we only care about buying at the lowest price and seeing if the highest selling point in the future is greater than the current maximum
"""
import sys
prices = [7,6,4,3,1]
def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy low, sell high. when there is lower price, keep the current profit and start new search for highest selling point.
        current_low = sys.maxsize #sets current low to highest possible value
        print(current_low)
        profit = 0
        for i in prices:
            if i < current_low:
                current_low = i
            elif i- current_low > profit:
                profit = i - current_low
        return profit

maxProfit(prices)

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