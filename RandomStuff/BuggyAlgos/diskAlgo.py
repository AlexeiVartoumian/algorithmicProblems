start= 189
tracks = [49, 116, 140, 32, 61, 117, 169, 101, 193, 178]

tracks2 = [32,49 ,61 , 101 , 116  , 117,140,169,178,193]

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

# brutalbug depending on where start pos is we will traverse upwards and visit all sequence elements.
#point is that when we go down we have to find trhe first element such that is smaller than starting position
#without calculating elements until we get there. 
def BrutalBugelevator(start, tracks2):
    visited = set()
    res = []
    index = 0
    for i in range(len(tracks2)-1):
        if tracks2[i] <start and tracks2[i+1] > start:
            res = tracks2[:i+1:] + [start] + tracks2[i+1::]
            index = i+1
    visited.add(start)
    asum = 0
    up = True
   
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
    for i in range(len(tracks2)-1):
        if tracks2[i] <start and tracks2[i+1] > start:
            res = tracks2[:i+1:] + [start] + tracks2[i+1::]
            index = i+1
    visited.add(start)
    asum = 0
    visited.add(start)
    while len(visited) != len(res):
        nextindex = ( (index+1) % len(res)) 
        print("the diff is :" , abs(res[index] - res[ nextindex]))
        asum  += abs(res[index] - res[ nextindex])
        visited.add(res[ nextindex])
        index = nextindex
    
    print(asum)
    return asum       
        
fifo(start,tracks)
BrutalshortestScanFirst(start,tracks)
BrutalBugelevator(start,tracks2)
cscanUp(start,tracks2)
