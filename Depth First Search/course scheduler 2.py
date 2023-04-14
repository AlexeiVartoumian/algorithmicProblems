"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

"""
This is a graph problem since each course is somehow connected to another. the idea is to start by creating an adjacenccy list for each node as in for each node show a list of nodes that are its prerequisites. If there are any cycles in the graph that means in order to take one course you need to take its prerequisite and vice versa , in which case its not possible to take al courses in which case return []. as such after building the adjacency list  you will need several varaibles output as a list, visited as a set to avoid repeated work a cycle set which keeps track of a current node being a prerequisite of a very node which is a prerequisite of that node. then apply depth first search on each node at the end of each iterations return true if no cycle is found and append node to output. finally do a final loop through the courses calling the dfs function which will append the node at every stage and also check if its a cycle= return empty array is that happens. if you reach the end of the loop that means  you can take all courses and return the result.
"""




def coursescheduler(numCourses, prerequisites):

    prereqs = {c:[] for c in range(numCourses)} # instantiate object adjacency list
    #for each course have array

    for course , prereq in prerequisites:
        prereqs[course].append(prereq) # loop through list and append prequisites to that object
    
    cycle = set()
    visited = ()
    res = []

    def dfs(course):
        if course in cycle:
            return False
        if course in visited:
            return True
        cycle.add(course)

        for pre in prereqs[course]:
            if dfs(pre) == False:
                return False
        
        cycle.remove(course)
        res.append(course)
        visited.add(course)
        return True

    for c in range(numCourses):
        if dfs(c) == False:
            return []
    return res





def findOrder(numCourses, prerequisites ):
          
        prereqs = {c:[] for c in range(numCourses)}

        for course, prereq in prerequisites:
           prereqs[course].append(prereq)
        
        res = []
        cycle = set()
        visited = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for pre in prereqs[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return res