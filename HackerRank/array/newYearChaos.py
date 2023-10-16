"""
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example
q = [1,2,3,5,4,6,7,8]
If person  bribes person , the queue will look like this: . Only  bribe is required. Print 1.

Person  had to bribe  people to get to the current position. Print Too chaotic.

Function Description

q = [4,1,2,3]
too choatic since 4 bribed way too manby people
Complete the function minimumBribes in the editor below.

minimumBribes has the following parameter(s):
int q[n]: the positions of the people after all bribes
Returns
No value is returned. Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than  people.
Input Format
The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.
"""

"""
my first approach was to check the indexes and any number greater
than index curindex +2 is false and to compute the number of bribes for any number that is in bounds.
but this failed a speicific kind of test case the one below
q = [1,2,5,3,7,8,6,4] where the above approach will give 6 but it is in fact 7. 
this is because 5 moves to pos 3 so bribes at that point is 2. 7 moves moves to pos 5 and 8 moves to pos 6. for a total of 6 moves the array will look like this
q = [1,2,5,3,7,8,4,6]
but the above approach does not consider numbers at indexes greater than thier start position but value being smaller than actual position as a result of larger numbers bribing away. the final result should look like q = [1,2,5,3,7,8,6,4] one more bribe took place.

as such the approach below was to start with a sorted array 1 to n and then apply the shifts so long as larger numbers satisfy not bribing too much. the question to ask here is does my sorted array have the correct number in place such that it is identical to query? if not then look forward and shift the numbers according to wether 1 or two bribes too place. return number of bribes.
"""

def minimumBribes(q):
    # Write your code here
    
    chaos = False
    bribes = 0
    startqueue = q.copy()
    startqueue.sort()
    for i in range(len(startqueue)):
        
        if startqueue[i] != q[i]:
            if (q[i] > i+ 1 ) and (q[i] - (i+1) ) >2:
                chaos = True
                print("Too chaotic")
                break
            else:
                count = i
                target = q[i]
                if startqueue[count+1] == target:
                        startqueue[count],startqueue[count+1] = startqueue[count+1],startqueue[count]
                        bribes+=1
                else:
                    bribes+=2
                    startqueue[count],startqueue[count+2] = startqueue[count+2],startqueue[count]
                    startqueue[count+2],startqueue[count+1] = startqueue[count+1],startqueue[count+2]
    if not chaos:
        print(bribes)            