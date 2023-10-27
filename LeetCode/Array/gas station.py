"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

"""
the first obeservation I made was that it is ony possible to start at an index where
gas[i] > cost[i]. building on that if the total sum of gas array is less then cost[i] then it doesnt matter where you start it simply will not be possible to consectutively visit each station without gas falling below zero.

as such my solution is not optimal but the what i did was store all indexes that are above the condition gas[i] - cost[i] as possible starting stations. after than loop thorugh the dicionary from that index and check one by one if runningsum ever falls below zer0. if it does it also means that all stations between starting index and index where sum falls below zeroare not possible to start from. use sets to keep track of that.

a far more optimal solution is using the concepts of the above without the data structures. just keeping a runningsum if it ever falls below zero then set result to to the next index where that happended. loop will only execute if sum of gas is less than sum of cost.
"""

def canCompleteCircuit(gas, cost):

        visited =set()

        totalgas = 0
        totalcost = 0
        possible = {}

        for i in range(len(gas)):
            totalgas+= gas[i]
            totalcost+= cost[i]
            if gas[i] < cost[i]:
                visited.add(i)
            else:
                
                possible[i] = (gas[i] - cost[i])
        
        if totalcost > totalgas:
            return -1
        
        for index,runningsum in possible.items():

            track = 1
            i= index
            if i not in visited:
                visited.add(index)
                falsepositive = set()
                while track != len(gas):
                    if i == len(gas)-1:
                        track+=1
                        i = 0
                        runningsum += (gas[i]-cost[i])
                        falsepositive.add(i)
                        if runningsum <0:
                            while falsepositive:
                                visited.add(falsepositive.pop())
                            break
                    else:
                        i+=1
                        track+=1
                        runningsum += (gas[i]-cost[i])
                        falsepositive.add(i)
                        if runningsum <0:
                            while falsepositive:
                                visited.add(falsepositive.pop())
                            break
                if track == len(gas):
                    return index
        return -1

def canCompleteCircuit(gas, cost) :
        if sum(gas) < sum(cost):
            return -1
            
        total = 0
        res = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res