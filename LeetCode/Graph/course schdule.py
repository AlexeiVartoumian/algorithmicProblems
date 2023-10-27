"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

"""
the goal is to find if a cycle exists in the graph. as such all courses without prequisites are singified with an empty array in the adjacency list. after that its using dfs where the base case is we have already visited a course before whci is makred with a visited set, the goal which is the second base case is to traverse with dfs such that we reach a course with an empty array. if this is possible then we remove from the visited array and set all courses were this was possible to mutate it to empty array. in the dfs function when iterating we check at every instance if the function call is true or not checking the above two base cases.
"""

def canfinish(numcourses,prerequisites):

    prereqsneeded = {course:[] for course in range(numcourses)}

    for i in range(len(prerequisites)):
        prereqsneeded[prerequisites[i][0]].append(prerequisites[i][1])
    visit = set()


    def dfs(key):
        if key in visit:
            return False
        if prereqsneeded[key] == []:
            return True
        visit.add(key)
        for m in prereqsneeded[key]:
            if not dfs(m):
                return False
        #since all possible routes have been determined all of these 
        #course are noe considered safe to take!
        visit.remove(key)
        prereqsneeded[key] = []

    for i in range(numcourses):

        if not dfs(i):
            return False

