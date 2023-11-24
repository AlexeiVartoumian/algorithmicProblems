"""
Your algorithms have become so good at predicting the market that you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be for the next number of days.

Each day, you can either buy one share of WOT, sell any number of shares of WOT that you own, or not make any transaction at all. What is the maximum profit you can obtain with an optimum trading strategy?

Example
prices = [1,2]
Buy one share day one, and sell it day two for a profit of 1. Return 1 .

prices = [2,1]
No profit can be made so you do not buy or sell stock those days. Return 0.

Function Description

Complete the stockmax function in the editor below.

stockmax has the following parameter(s):

prices: an array of integers that represent predicted daily stock prices
Returns

int: the maximum profit achievable

Constraints
1<=t<=10
1<=n<=50000
1<=prices[i]<=100000
"""

"""
this problem wants to compute for each day the best return.
my first approachw as to do a greedy sum on each day asking the question
is profit on this day greater than greatest profit seen so far?
this question is formed as max( maxProfitForDay , profit[j] - profit[i]) where j is a later day then i. I would compute this for every day then go through all the sums adding it to total profit. this is N^2 though and exceeded the time limits.

The second approach I took and the one that passed was to ask how many times do I really need to find the best day j for a given previous day i. because I greedily require the highest j possible for a given i all consequent i's [i+1,i+2,i+3] <= j will have this day j as the best possible day to sell.
therefore I do not have to compute the best day to sell for every i only when i goes past the post where the largest seen j was. 
"""
def stockmax(prices):
    # Write your code here
    index = 0
    
    maxprofit = 0
    for i in range(len(prices)-1):
        
        if i >= index:
            maxprofitforday = 0
            for j in range(i+1, len(prices)):    
                if prices[j] - prices[i] >= maxprofitforday :
                    maxprofitforday = prices[j] - prices[i]
                    index = j
        if i < index:            
            maxprofit += prices[index] - prices[i]
    return maxprofit


#ineffecient answer
def bigprofit(n, prices):
    
    indexes= {}
    
    for i in range(len(prices)-1):
        
        maxprofitsofar  = 0
        for j in range(i+1, len(prices)):
            
            maxprofitsofar = max(maxprofitsofar, prices[j] - prices[i])
            
        
        indexes[i] = maxprofitsofar
    totalsum = 0
    for i,x in indexes.items():
        totalsum+=x
    
    return totalsum
