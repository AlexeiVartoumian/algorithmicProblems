"""
A queue is an abstract data type that maintains the order in which elements were added to it, allowing the oldest elements to be removed from the front and new elements to be added to the rear. This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue (i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

1 x: Enqueue element  into the end of the queue.
2: Dequeue the element at the front of the queue.
3: Print the element at the front of the queue.
Input Format

The first line contains a single integer, , denoting the number of queries.
Each line  of the  subsequent lines contains a single query in the form described in the problem statement above. All three queries start with an integer denoting the query , but only query  is followed by an additional space-separated value, , denoting the value to be enqueued.
"""

"""
below is using array slicing where adding to the queue takes advantage of normal list behaviour and removing from the queue is the array slice from index 1 onwards. to simulate commands as a string to be parsed that was in arg form just map all the input into a list turning all elements into a interger beforehand and separating by whitespace which is determined by the input function. we know right away if the length of an argument is greater than 1 it must be a value so handle that other wise whatever the value the query is execute that command
"""
n = int(input())
class Queue:

    def __init__(self):
        self.items = []
    
    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):

        if not self.items:
            return "no items to remove from queue"
        return self.items[1::]
    
    def gethead(self):
        if not self.items[0]:
            return "queue empty"
        return self.items[0]
    def getsize(self):
        return len(self.items)
    def isempty(self):
        return len(self.items) == 0


queue = Queue()

for _ in range(n):
    args= list(map(int,input().split()))

    if len(args)> 1:
        queue.enqueue(args[1])
    else:
        arg = args[0]
        if arg == 2:
            queue.dequeue()
        elif arg == 3:
            print(queue.gethead())