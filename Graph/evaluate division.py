"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""
"""
the solution and idea behind this problem is beautiful! looking at the values and the equations an initial observation can be made where given two 
equations we want all terms such that share a term in the denominator as well as in the numerator. after knowing this that term will cancel out.
suppose the first input where a/b = 2 and b/c = 3. well to get a/c since both share the b in the denominator and numerator respectively you can simply multiply the two terms. in fact you can say that given a starting node a which points to b , if b points to c then there is a path that exists from a to b. THIS MAKES THIS A GRAPH QUESTION. the beautiful part of framing the problem this way is that consequently the path from c to b to a will be the inverse of the path between two nodes where an equation is given which can be expressed as 1/value[i].
after knowing this its a case of generating the adjacency list with any node pointing to another node and the corresponding value found in values and the inverse of that with the inverse of the value being 1/value.

then for all queries perform depth first search where we treat the first half of the quesry as the source and the second half of the query as the target with the aim of returning a value that will be either -1 meaning no equation can found in the adjacencylist or a different value , meaning it is possible to create a new equation from the information given. to avoid cycles have a visited set as well as make sure to use a loop in the dfs since a given letter may have more then one equation.
"""


def calc(equations, values, queries):
    book = dict()

    for (node,nextnode), value in zip(equations, values):
        
        if node not in book:
            book[node] = []
        if nextnode not in book:
            book[nextnode] = []
        
        book[node].append((nextnode,value))
        book[nextnode].append((node,1/value))
    

    def dfs(source,target,runningsum,seen):

        if source not in book or target not in book:
            return -1 
        if source in seen:
            return -1

        if source == target:
            return runningsum

        seen.add(source)

        for node,nextvalue in book[source]:

            if node not in seen:

                finalvalue = dfs(node,target,runningsum*nextvalue,seen)
                if finalvalue != -1:
                    return finalvalue
        return -1
    
    results = []

    for source,target in queries:
        seen = set()
        results.append(dfs(source,target,1,seen))
    return results


"""
class Solution:
    def calcEquation(self, equations values, queries: List[List[str]]) -> List[float]:

       
        book = dict()

        for (node,nextnode),value in zip(equations,values):
            if node not in book:
               book[node] = []
            
            if nextnode not in book:
                book[nextnode] = []
            
            book[node].append((nextnode,value))
            book[nextnode].append((node,1/value))
        
        def dfs(source,target,runningsum,seen):
            if source not in book or target not in book:
                return -1
            
            if source == target:
                return runningsum
            seen.add(source)

            for nextnode, nextvalue in book[source]:

                if nextnode not in seen:
                    val = dfs(nextnode,target,runningsum*nextvalue,seen)
                    if val != -1:
                        return val

            return -1 


        results = []

        for source, target in queries:
            seen = set()
            results.append(dfs(source,target,1,seen))
        
        return results
"""