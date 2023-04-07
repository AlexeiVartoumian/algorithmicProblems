"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""



"""
brute force approach is to compare every combination value with each other and to compute the given largest area which will be the minumum value between those two points mulitiplied by the respective distance between those two points. however this is quadratic in time. the optimal approach is to use two pointers. since width of the two points is a determining factor the idea is to two use pointers left and right. left will be at the very beginnning of the array whereas right will be at the very end. after that you close the size of the window by first computing and comparing which area size value is greater . after that if the leftpoint value  is smaller or equal t0 than the right point value increment it. if the rightpoint value is smaller than decrement it. keep doing this until left has passed right.
"""
def area(height):

    left = 0
    right = len(height)-1

    curarea = min(height[left],height[right]) * (right-left)

    while left < right:

        curarea = max(min(height[left],height[right]) * (right-left), curarea)

        if height[left] <= height[right]:
            left+=1
        else:
            right -=1
    
    return curarea

"""
brute force approach
    res = 0
    
    for i in range(len(height)):
        
        for j in range(i+1,len(height)):
            curarea = (j-i) * min(height[i],height[j])
            res = max(curarea,res)
    """      

def maxArea(height):

        left = 0
        right = len(height)-1

        curarea = min(height[left],height[right]) * (right-left)

        while left < right:
            
            curarea = max(min(height[left],height[right])* (right-left), curarea )

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        
        return curarea    