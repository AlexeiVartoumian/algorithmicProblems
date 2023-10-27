"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
"""

"""
I used sets to tackle this problem since there can only ever be one town judge .  having a adjcacencylist with keys 1 to n and having a set as a value. my apporach was clumsy and by process of elmination starting with 1 , n elments in a set called town judge basically loop thorugh the adjacencylist and see if a given element exists in that adj list set - if not remove it.
if a given set is empty in the adj list and its not in the townjudge set that means a person does not trust the possible townjudge and immediately return -1. otherwise if length of set is 2or more or 0 then reutrn -1. finally return the townjudge of single element in set.

alternarively and way better is just use a visited array numbered from 1 to n. then loop through the trust array decrementing the 0 element at that position in the visited array and incrementing the 1 element . finally loop through the visited array , if any element is equal to n-1 then that is the town judge.
"""
from collections import defaultdict
def findJudge(n, trust) :
        adjacencylist = defaultdict(set)
        townjudge = set()
        remove = set()
        items = set()
        if not trust and n == 0:
            return -1
        elif n == 1:
            return 1
        for i in range(1,n+1):
            townjudge.add(i)
            remove.add(i)
            adjacencylist[i]
        for i in range(len(trust)):
            adjacencylist[trust[i][0]].add(trust[i][1])
        
        for i,x in adjacencylist.items():
            if not x:
                if i not in townjudge:
                    return -1
            else:
                for j in remove:
                    if j not in adjacencylist[i]:
                        items.add(j)
                        townjudge.discard(j)
                for item in items:
                    remove.discard(item)
                items = set()
        
        if len(townjudge) > 1 or len(townjudge) == 0 :
            return -1
        for j in townjudge:
            return j

def findJudge(n, trust):
        
        count = [0 for i in range(n+1)]
        print(count)
        for p1, p2 in trust:
            count[p1]-=1
            count[p2]+=1
        
        for i in range(1,len(count)):
            if count[i]==n-1:
                return i

        return -1     