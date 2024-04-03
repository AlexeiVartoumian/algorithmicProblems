"""
Consider the following string of page references 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2. Complete a table
showing the frame allocation assuming 3 page frames and calculate the hit rate for the following
scheduling algorithms:
(a) Optimal
(b) Least Recently Used
(c) FIFO

"""
from collections import defaultdict
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]

numpageFrames = 3

cache = [-1] * numpageFrames
leastRecentcache = [-1] * numpageFrames

optimalmatrix = [[-1] * len(pages) for  i in range(numpageFrames)]
lrumatrix = [[-1] * len(pages) for  i in range(numpageFrames)]

optimalindexes = defaultdict(list)

faults = [-1] * len(pages)
lrufaults = [-1] * len(pages)
lruCache = defaultdict(int)

for i in range(len(pages)):
    optimalindexes[pages[i]].append(i)

def update(i , matrix,cache):
    
    for z in range(len(matrix)):
        matrix[z][i] = cache[z]
print(optimalindexes)
print(optimalmatrix)
print(update(0 , optimalmatrix, cache))

def optimal(indexes, number,cache):

    smallest = len(indexes)
    curnum = -1
    for i in range(len(cache)):
        if len(indexes[cache[i]])< smallest:
            smallest = len(indexes[cache[i]])
            curnum = cache[i]
    for j in range(len(cache)):
                if cache[j] == curnum:
                    cache[j] = number
    return cache

def lru(lruCache, number,leastRecentcache):
     
    smallest = 0
    curnum = -1
    for i in range(len(leastRecentcache)):
        if lruCache[leastRecentcache[i]] > smallest:
             smallest = lruCache[leastRecentcache[i]]
             curnum = leastRecentcache[i]
    for j in range(len(leastRecentcache)):
         if leastRecentcache[j] == curnum:
              del(lruCache[curnum])
              leastRecentcache[j] = number
    return leastRecentcache

def updatelruRecords(lruCache):

    for i in lruCache:
        lruCache[i]+=1
    return lruCache

for i in range(len(pages)):
    
    if pages[i] not in cache:
       
        if -1 in cache:
            for j in range(len(cache)):
                if cache[j] == -1:
                    cache[j] = pages[i]
                    break
            
            optimalindexes[pages[i]] = optimalindexes[pages[i]][1::]
            update(i , optimalmatrix , cache)
        else:
            cache = optimal(optimalindexes,pages[i], cache)
            optimalindexes[pages[i]] = optimalindexes[pages[i]][1::]
            update( i , optimalmatrix ,cache) 
    else:
        for z in range(len(cache)):
             optimalmatrix[z][i] = cache[z]
        faults[i] = 1

# for i in range(len(pages)):
#     if pages[i] not in leastRecentcache:
#         print(pages[i] , "needs to evict someone" , lruCache)
#         if -1 in leastRecentcache:
#             for j in range(len(leastRecentcache)):
#                 if leastRecentcache[j] == -1:
#                     leastRecentcache[j] = pages[i]
#                     break
            
            
#             lruCache[pages[i]] = 0
            
#             lruCache=  updatelruRecords(lruCache)
           
#             update(i , lrumatrix , leastRecentcache)
#         else:
            
#             leastRecentcache = lru(lruCache, pages[i],leastRecentcache)
#             print(leastRecentcache)
#             update( i , lrumatrix ,leastRecentcache) 
#     else:
#         for z in range(len(leastRecentcache)):
#              lrumatrix[z][i] = leastRecentcache[z]
#         lrufaults[i] = 1

# for i in lrumatrix:
#     print(i)
for i in optimalmatrix:
    print(i)

print(faults)

pageFaults = 0
pageHits = 0

for i in faults:
    if i == 1:
          pageHits+=1
    else:
         pageFaults+=1

print(pageHits , pageFaults)

