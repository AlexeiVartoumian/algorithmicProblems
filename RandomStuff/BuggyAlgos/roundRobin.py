from collections import deque
from collections import defaultdict

## only handles quantum = 1
# arrivalTime = [0,1,3,9,12]
# timetoProc = [3,5,2,5,5]

# arrivalTime = [6, 9, 8,5, 4, 8, 0, 10, 3] 
# timetoProc = [7, 1, 9, 5, 11, 7, 2, 10, 8]

arrivalTime = [2, 1, 0]
timetoProc= [ 8, 4, 8]

# arrivalTime = [0, 1, 2,3]  
# timetoProc =[3, 2, 3, 3]

quantum = 1


queue = deque()


arriveToProc = defaultdict(list)
procTotime = defaultdict(int)
processToArrival = defaultdict(int)

def initTable(timeToProc , arrivalTime, processToArrival):

    for i in range(len(arrivalTime)):

        letter = chr(i + 65)
        arriveToProc[arrivalTime[i]].append(letter)
        procTotime[letter] = timeToProc[i]
        processToArrival[letter] = arrivalTime[i]
    
    

#need to sort arrival time to proc dic according
def sort(arrivalTime):
    return arrivalTime.sort()

def checkcount( count , arriveToProc):

    return count in arriveToProc


initTable(timetoProc, arrivalTime, processToArrival)

print(arriveToProc)
print(procTotime)
print(processToArrival)

count = 0
total = 0
#while procTotime:

turnaroundtime = defaultdict(int)
for i in range(100):
        
        count+=quantum
        if i in arriveToProc:
            for j in range(len(arriveToProc[i])):
                queue.append(arriveToProc[i][j])
        if queue:
        
            currentProc = queue.popleft()
            if procTotime[currentProc]> 0:
                queue.append(currentProc)
            if total >= len( arrivalTime):
                break
            if queue:
                procTotime[queue[0]]-= quantum

                if procTotime[queue[0]] <=0:
                    total+=1
                    # print( queue[0] , "done at " ,i )
                    # print(count)
                    # print("turnaround time : "  , (count - processToArrival[queue[0]] ))
                    #turnaroundtime[queue[0]] = i - processToArrival[queue[0]]  + 1
                    turnaroundtime[queue[0]] = (count) - processToArrival[queue[0]]  
print(turnaroundtime)
asum = 0
for i in turnaroundtime:
    asum+= turnaroundtime[i]

print(asum / len(turnaroundtime ) * quantum)

    
