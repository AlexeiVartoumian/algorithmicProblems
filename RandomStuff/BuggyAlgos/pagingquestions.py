"""
Consider the following string of page references 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2. Complete a table
showing the frame allocation assuming 3 page frames and calculate the hit rate for the following
scheduling algorithms:
(a) Optimal
(b) Least Recently Used
(c) FIFO

"""
from collections import defaultdict
#pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
#pages = [15, 1, 9, 13, 13, 15, 9, 10, 6, 7, 15, 6, 4]
#pages =  [3, 5, 7, 1, 15, 14, 11, 3, 4, 7, 15, 4, 10, 4, 10]
#pages = [ 6, 14, 12, 1, 5, 15, 5, 2, 11, 13, 7, 8, 1]
#pages = [10, 9, 6, 5, 6, 6, 6, 7, 9, 5, 10, 14, 11, 6, 3, 1]
#pages = [ 3, 12, 6, 6, 5, 8, 13, 5, 7, 7, 14, 12, 7, 13, 3, 9]
pages = [4, 3, 7, 4, 10, 12, 4, 11, 8, 12, 7, 12, 8, 5, 4, 2, 15, 10, 14,
13, 8, 1, 2, 2]
pages = [6, 14, 12, 1, 5, 15, 5, 2, 11, 13, 7,
8, 1]
numpageFrames = 4

cache = [-1] * numpageFrames
leastRecentcache = [-1] * numpageFrames
fifocache = [-1] * numpageFrames

optimalmatrix = [[-1] * len(pages) for  i in range(numpageFrames)]
lrumatrix = [[-1] * len(pages) for  i in range(numpageFrames)]

fifomatrix = [[-1]* len(pages) for i in range(numpageFrames)]


optimalindexes = defaultdict(list)
lrurecord = defaultdict(int)
fiforecord = defaultdict(int)

faults = [-1] * len(pages)
lrufaults = [-1] * len(pages)
fifofaults = [-1] * len(pages)

for i in range(len(pages)):
    optimalindexes[pages[i]].append(i)

def update(i , matrix,cache):
    
    for z in range(len(matrix)):
        matrix[z][i] = cache[z]
# print(optimalindexes)
# print(optimalmatrix)
# print(update(0 , optimalmatrix, cache))

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

def lru(lrurecord, number,leastRecentcache):
     
    smallest = 0
    curnum = -1
    for i in range(len(leastRecentcache)):
        if lrurecord[leastRecentcache[i]] > smallest:
             smallest = lrurecord[leastRecentcache[i]]
             curnum = leastRecentcache[i]
    #print("evicting: " ,curnum , "  wth dist" , smallest )         
    for j in range(len(leastRecentcache)):
         if leastRecentcache[j] == curnum:
              del(lrurecord[curnum])
              leastRecentcache[j] = number
              lrurecord[number] = 0
              break
    return leastRecentcache
def fifo(fiforecord , number , fifocache):
    smallest = 0
    curnum = -1
    for i in range(len(fifocache)):
         if fiforecord[fifocache[i]] > smallest:
              smallest = fiforecord[fifocache[i]]
              curnum = fifocache[i]
    for j in range(len(fifocache)):
         if fifocache[j] == curnum:
              del(fiforecord[curnum])
              fifocache[j] = number
              fiforecord[number] = 0
              break
    return fifocache
def updatelruRecords(lrurecord):

    for i in lrurecord:
        lrurecord[i]+=1
    return lrurecord
def updateoptimalRecords(optimalindexes, curindex):
     
    for i in optimalindexes:
         if optimalindexes[i] and  optimalindexes[i][0] <= curindex  : 
            optimalindexes[i] =  optimalindexes[i][1::]
    return optimalindexes
for i in range(len(pages)):
    
    if pages[i] not in cache:
        
        if -1 in cache:
            for j in range(len(cache)):
                if cache[j] == -1:
                    cache[j] = pages[i]
                    break
            #optimalindexes[pages[i]] = optimalindexes[pages[i]][1::]
            update(i , optimalmatrix , cache)
        else:
            cache = optimal(optimalindexes,pages[i], cache)
            #optimalindexes[pages[i]] = optimalindexes[pages[i]][1::]
            update( i , optimalmatrix ,cache) 
    else:
        for z in range(len(cache)):
             optimalmatrix[z][i] = cache[z]
        faults[i] = 1
    indexes = updateoptimalRecords(optimalindexes, i)

for i in range(len(pages)):
    if pages[i] not in leastRecentcache:
        #print(pages[i] , "needs to evict someone" , lrurecord)
        if -1 in leastRecentcache:
            for j in range(len(leastRecentcache)):
                if leastRecentcache[j] == -1:
                    leastRecentcache[j] = pages[i]
                    break    
            lrurecord[pages[i]] = 0
            lrurecord=  updatelruRecords(lrurecord)
            update(i , lrumatrix , leastRecentcache)
        else:
            
            leastRecentcache = lru(lrurecord, pages[i],leastRecentcache)
            #print(leastRecentcache)
            updatelruRecords(lrurecord)
            update( i , lrumatrix ,leastRecentcache) 
    else:
        for z in range(len(leastRecentcache)):
             lrumatrix[z][i] = leastRecentcache[z]
        lrurecord[pages[i]] = 0
        updatelruRecords(lrurecord)
        lrufaults[i] = 1

for i in range(len(pages)):
    if pages[i] not in fifocache:
        if -1 in fifocache:
            for j in range(len(fifocache)):
                if fifocache[j] == -1:
                    fifocache[j] = pages[i]
                    break    
            fiforecord[pages[i]] = 0
            fiforecord=  updatelruRecords(fiforecord)
            update(i , fifomatrix , fifocache)
        else:
            fifocache = lru(fiforecord, pages[i],fifocache)
            
            fiforecord = updatelruRecords(fiforecord)
            update( i , fifomatrix ,fifocache) 
    else:
        for z in range(len(leastRecentcache)):
             fifomatrix[z][i] = fifocache[z]
        
        fiforecord = updatelruRecords(fiforecord)
        fifofaults[i] = 1 

nums = ["{:>2}".format(number) for number in pages]
print(nums)
print("FifoMatrix:")


for i in fifomatrix:
    #print(i)
    formatted_numbers = ["{:>2}".format(number) for number in i]
    print(formatted_numbers)
fifohits = 0
fifobadfaults = 0
for i in fifofaults:
    if i == 1:
          fifohits+=1
    else:
         fifobadfaults+=1
print(fifohits, fifobadfaults)
print("######################")
print(" ")    
print(nums)
print("LruMatrix")

for i in lrumatrix:
    #print(i)
    formatted_numbers = ["{:>2}".format(number) for number in i]
    print(formatted_numbers)
lruhits = 0
randomfault = 0

for i in lrufaults:
    if i == 1:
          lruhits+=1
    else:
         randomfault+=1
print(lruhits, randomfault)
print("######################")
print(" ")
print(nums) 
print("optimalMatrix")

for i in optimalmatrix:
    #print(i)
    formatted_numbers = ["{:>2}".format(number) for number in i]
    print(formatted_numbers)

pageFaults = 0
pageHits = 0
for i in faults:
    if i == 1:
          pageHits+=1
    else:
         pageFaults+=1
print(pageHits, pageFaults)
print("######################")
print(" ")    


