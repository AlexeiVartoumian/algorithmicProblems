"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news.
Example 1:
Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
Example 2:
Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
"""

"""
this is a bfs or dfs traversal algorithm with a minor adjustment taking account the 
weight of  a a given manager(node) to inform subordinates. the thing to be careful of here is that we want the maximal value of a given value added to the total time it takes to inform all employees.
"""
from collections import defaultdict
from collections import deque
def numofminutes(n,headID,manager,informTime):
    records = defaultdict(list)

    queue = deque()
    for i in range(len(manager)):
        records[manager[i]].append(i)
    
    queue.append((headID,0)) # starting at zero since headmanager takes zero time to inform themselves

    total = 0

    while queue:
        #a traversal of length queue or keeping a visited set is not required
        #since we have a heirarchcal tree structure meaning the first time
        #we see a node will be only time we see a node

        curmanager,calctime = queue.popleft()

        if records[manager]:
            for i in range(len(records[curmanager])):
                queue.append((records[curmanager][i],calctime+informTime[curmanager])) #keep a runningsum of the cost of informing a given node of a given level
                #keeping in mind we want maximal weight
        else:
            total = max(total,calctime)
    return total

def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        records = defaultdict(list)
    
        queue = deque()
    
        for i in range(len(manager)):
            records[manager[i]].append(i)
    
        queue.append((headID, 0))
        total = 0
        while queue:
       
            curmanager ,calctime = queue.popleft()
        #currenttime = calctime +informTime[curmanager]
       
            if records[curmanager]:
                for i in range(len(records[curmanager])):
                    queue.append((records[curmanager][i], calctime+informTime[curmanager]))
            else:
                total = max(total,calctime)
        return total