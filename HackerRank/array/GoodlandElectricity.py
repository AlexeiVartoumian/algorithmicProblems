"""
Goodland is a country with a number of evenly spaced cities along a line. The distance between adjacent cities is 1 unit.

There is an energy infrastructure project planning meeting, and the government needs to know the fewest number of power plants needed to provide electricity to the entire list of cities. Determine that number. If it cannot be done, return -1.
You are given a list of city data. Cities that may contain a power plant have been labeled 1.
Others not suitable for building a plant are labeled 0. Given a distribution range of k, find the lowest number of plants that must be built such that all cities are served. The distribution range limits supply to cities where distance is less than k.
"""


"""
6 2           arr[] size n = 6, k = 2
0 1 1 1 1 0   arr = [0, 1, 1, 1, 1, 0]
Sample Output

2
"""
"""
Explanation

Cities c[1],c[2] ,c[3] , and c[4]  are suitable for power plants. Each plant will have a range of k=2. If we build in cities  2 cities,  c[1] and , c[4] then all cities will have electricity.
"""

"""
this question made me fail towards the solution. at first I thought the way to go was to greedily cacluate min range where
i will go backwards hit the first one and continue on my journey.
this was riddled with edge cases. what if i go back and there are no powerstations but there is one ahead? then I need to check ahead now. trying to run with this idea i kept falling into edgecases keeping track of the nearest 1 relative to a given zero adding it to vistied if in range what if i had a burst of 1' and 0's followed by nothing but ones.I had the wrong implementation

in the end the greedy approach is the right intition where we need to instead think of a pointer that needs to get past the end goal.We can say at the beginning we have not seen any cities and that therefore the maximum inclusive range will be (0 + k-1).
in order to move the pointer at the first pass we greedily set it to the width of k scanning all previous elements beforehand inlcuding start postion.
the first 1 we increment the counter and are allowed to shift our pointer by k + current index spaces. in other words we repeat the above by setting our pointer out of of previous pylon in effect restarting our array at that incremented index and asking the same question. the case where the pointer exceeds the length of the array we will have the minumum number of pylons needed to spread electricty. return -1 otherwise.
"""

def pylon(k , arr):

    count = 0
    flag = True
    pointer = 0

    while (pointer < len(arr)):

        flag = True
        # here we say start at max pos index , go down to current number
        for i in range(k-1,-k,-1):

            #check if in bounds
            if (i + pointer) >= 0 and (i +pointer) < len(arr) and arr[i + pointer] == 1:
                
                #greedily reset the bounds to next max range post to check
                pointer += (k + i)
                count+=1
                flag = False
                break
        if flag:
            return -1
    return count