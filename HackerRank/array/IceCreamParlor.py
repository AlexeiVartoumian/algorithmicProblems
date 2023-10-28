"""
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of money and the cost of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.

Example



They would purchase flavor ID's  and  for a cost of . Use  based indexing for your response.

Note:

Two ice creams having unique IDs  and  may have the same cost (i.e., ).
There will always be a unique solution.
Function Description

Complete the function whatFlavors in the editor below.

whatFlavors has the following parameter(s):

int cost[n] the prices for each flavor
int money: the amount of money they have to spend
Prints

int int: the indices of the two flavors they will purchase as two space-separated integers on a line
"""
"""
this a fancy way of describing twp sum. my approach 
is to store the complement as the key relative to money and
the  index as the value. Since the ice cream parlor cant give you money to
eat thier ice cream I dont have to handle negative values
"""

def whatFlavors(cost, money):
    # Write your code here
    
    
    values = {}
    for i in range(len(cost)):
        if cost[i] in values:
            print(values[cost[i]], i+1) 
        if cost[i] < money:
            complement = abs(money -cost[i])
            values[complement] = i+1