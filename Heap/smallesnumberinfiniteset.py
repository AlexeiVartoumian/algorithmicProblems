"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""

"""
going by the methods of addback and  popSmallest the method addback is called if and only if it already exists in the min heap which is kep track of by a minimum number. as such the class is initalised with the following strucutre self.min = 1 and self.heap = []. for the pop methood if the heap/arraylise structure exists then use the heappop methods to return the smallest number and increment the smallest number.
"""
from collections import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.min = 1
        self.heap = []
    
    def popSmallest(self)-> int:

        if self.heap:
            return heapq.heappop(self.heap)

        self.min+=1
        return self.min -1

    def addBack(self,num:int) -> None:

        if num < self.min and num not in self.heap:
            heapq.heappush(self.heap,num) 