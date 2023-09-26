"""
You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Check out the image below for better understanding:
"""
"""
this is an interval question. the first observation is that at the most elementary level the maximal jump will be 2 as in if the input array was [1] (fitting the constraint) then starting at zero to jump over this with minimal jump is 2. after this observation  approach was to sort the numbers  as store them in a separate set. then the idea is to try and pass the last element of array with the jump of interval starting at 2. if cur index is in the set then keep iterating until you reach a number that is not. but there is also the point to consider if the amount it took to get to that number when added to the current interval does not violate starting from zero rule. keep repeating until succesfully passing last elemetnt.
"""

def solution(inputArray):
    inputArray.sort()
    numbers = set(inputArray)
    maxjump = 2
    count = 0
    
    while count <= inputArray[-1]:
        
        count+= maxjump
        
        if count in numbers:
            temp = 0
            
            while count in numbers or (0 + maxjump+temp) in numbers:
                
                count+=1
                temp+=1
                
                if count > inputArray[-1]:
                    break
            
            count = 0
            maxjump+=temp
    return maxjump