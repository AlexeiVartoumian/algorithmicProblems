"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""

"""
Its important to ask before hand if  negative asteroids are added to the stack as ther are a few more edge cases to consider is this is the case. keeping mind that negative asteroids will always go left and positive asteroids will always go right a collision can only ever happen if a powsitive comes beofre a negative.
"""


def asteroidCollision(asteroids):

        stack = []

        for a in asteroids:
            while stack  and a < 0 and stack[-1] > 0:
                difference = a + stack[-1]

                if difference< 0:
                    stack.pop()
                elif difference> 0:
                    a = 0
                else:
                    a= 0
                    stack.pop()
            if a:
                stack.append(a)
         
        return stack

def asteroidCollision(asteroids):

        stack = []

        for a in asteroids:

            if a > 0:
                stack.append(a)
            
            elif not stack or  stack[-1] < 0 and a < 0:
                stack.append(a)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop()
                
                if stack and stack[-1]>0 and stack[-1] == abs(a):
                    stack.pop()
                elif stack and stack[-1] < 0 :
                    stack.append(a)
                elif not stack:
                    stack.append(a)
        
        return stack