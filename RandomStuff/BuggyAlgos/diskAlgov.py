

start = 116
#track3 = [55,58,39,18,90,160,150,38,184]
#track3 = [138, 28, 126, 88,95, 66, 98, 168, 153, 55]
#track3 =  [134, 132, 109, 5, 21,67, 12, 107, 64, 45]
track3 = [155, 14, 118, 96,104, 172, 83, 195, 93, 43]
#cscan is not yet correct
def fifo(start, tracks):
    
    asum = 0
    for i in range(len(tracks)):
         asum+= abs(start - tracks[i])
         start = tracks[i]
    print(asum)

def BrutalshortestScanFirst(start, tracks):
    asum = 0
    visited = set()
    while len(visited) != len(tracks):
        diff = 200000000 
        marker = 0
        for i in range(len(tracks)):
            if abs(start -tracks[i] ) < diff and tracks[i] not in visited:
                diff = abs(start -tracks[i] )
                marker= tracks[i]
        asum+= abs(start -marker )
        start = marker
        visited.add(marker)
    print(asum)


def BrutalBugelevator(start, tracks2):
    visited = set()
    res = []
    index = 0
    tracks2.sort()
    up = True
    if  start < tracks2[0]:
            res = [start] + tracks2
                
    elif start > tracks2[-1]:
        res = tracks2 + [start]
        index = len(res)-1
        up = False
    else:
        for i in range(len(tracks2)-1):
            if tracks2[i] <start and tracks2[i+1] > start:
                res = tracks2[:i+1:] + [start] + tracks2[i+1::]
                index = i+1
                break
       
    visited.add(start)
    asum = 0
    
    
    
    prev = index
    while len(visited) != len(res):
        if up:
            if index < len(res)-1:
                print("the diff is :" , abs(res[prev] - res[index+1]))
                asum+= abs(res[prev]- res[index+1])
                index +=1
                prev = index
                
                visited.add(res[prev])
            else:
                up = False
        else:
            if index >= 0 and res[index-1] not in visited:
                print("the diff is :" , abs(res[prev] - res[index-1]))
                asum+= abs(res[prev] - res[index-1])
                visited.add(res[index-1])
                prev = index-1
            index-=1
    print(asum)



# here I dont check if i have already visited elements because I am only going in one direction.
# I only care about visiting all the elements after starting poisition has been inserted
def cscanUp(start,tracks2):
    visited = set()
    res = []
    index = 0
    tracks2.sort()
    if  start < tracks2[0]:
            res = [start] + tracks2
                
    elif start > tracks2[-1]:
        res = tracks2 + [start]
        index = len(res)-1
        up = False
    else:
        for i in range(len(tracks2)-1):
            if tracks2[i] <start and tracks2[i+1] > start:
                res = tracks2[:i+1:] + [start] + tracks2[i+1::]
                index = i+1
            
    visited.add(start)
    asum = 0
    visited.add(start)
    print(res , " is ")
    while len(visited) != len(res):
        nextindex = ( (index+1) % len(res)) 
        print("the diff is :" , abs(res[index] - res[ nextindex]))
        asum  += abs(res[index] - res[ nextindex])
        visited.add(res[ nextindex])
        index = nextindex
    
    print(asum)
    return asum
        
# fifo(start,tracks)
# BrutalshortestScanFirst(start,tracks)
# BrutalBugelevator(start,tracks2)
# cscanUp(start,tracks2)

print("fifo")
fifo(start,track3)
print("ssf")
BrutalshortestScanFirst(start,track3)
print("scan")
BrutalBugelevator(start,track3)
print("c-scan")
cscanUp(start,track3)

