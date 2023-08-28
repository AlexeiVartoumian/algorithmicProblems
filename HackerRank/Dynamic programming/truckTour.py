"""
Suppose there is a circle. there are n petrol pumps on that circle. petrol pumps are numbered 0 to n-1 inclusive. you have tow peices of information corresponding to each of the petrol pump (1): the amount of petrol the particular pump will give.
2) the distance from that petrol pump to the next petrol piump. intially you have a tank of infinite capacity carrying no petrol, you can start the tour at any of the pterol pumps. calculate the first point from where the truck will be able to complete the circle. consider that the truck will stop at each of the petrol pumps. the truck will move one kilometeer for each liter of the petrol.
"""
"""
test case input:
3--------> number of pumps
1  5 -----> digit1 amount of petrol fuel digit2 : distance to next station
10 3
3  4
"""

"""
this is a dynamic programming style problem. we are only dealing with positive integers which is fortunate as having a petrol pump that siphons petrol from the tank will be unfair as well as increasing the complexity of the problem. as such the approach is to ask at every step starting at the very first step with the following given : "intially you have a tank of infinite capacity carrying no petrol". at the first pass compute the balance which will be the amount of petrol minus the distance and add that to the balance as a running sum. if that sum falls below zero then the following has happened; we are at a petrol pump where the distance is greater than the what is in the tank plus what is in the pump.
CONSEQUENTLY what that means is that all indexes up to and including where the balance fell below zero can be counted out. the next possible earlist index will be the one ahead and repeat process. return index.
"""

def truckTour(petrolpumps):
    # Write your code here
    
    index = 0
    gas = 0
    for i in range(len(petrolpumps)):
        gas += petrolpumps[i][0] - petrolpumps[i][1] 
        if gas <0:
            gas = 0
            index = i+1
    return index