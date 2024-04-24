from collections import deque

Resources = input("please enter avaliable resources with space delimiter")

numProcces = input("please enter number of processes")


def splitinto(string):

    string = string.strip()
    return [ int(i)  for i  in string.split(" ")]

numResources= splitinto(Resources)
originalResources = numResources.copy() # will be manipulating num resources
numProcs = [i for i in range( int(numProcces))]
print(numResources , numProcs)

def allocate(numResources , numProcs):
    matrix = []
    for i in range(len(numProcs)):
        matrixval = []
        thing = input("please allocate")
        try:
            stuff =  insert(thing, numResources, i)
            numResources = stuff[0]
            matrixval = stuff[1]
        except:
            print(insert(thing, numResources, i))
            return 
        matrix.append(matrixval)
    return matrix

        

def insert(thing , numResources, proc):
    vals = splitinto(thing)
    print(vals , numResources , " haha")
    if len(vals) > len(numResources):
        raise ValueError("cant be done")
    matrixval = []
    print(numResources , "before")
    for i in range(len(vals)):
        if numResources[i] < vals[i] or numResources[i]-vals[i] < 0:
            raise ValueError(  "cant be done resource " , i , " has available" , numResources[i] , "and proc " ,  proc , "wants" , vals[i] , " of it")
        matrixval.append(vals[i])
        numResources[i]-= vals[i]
    print(numResources , "after")
    return (numResources, matrixval)

def claim(numProcs , numResources):
    matrix = []
    for i in range(len(numProcs)):
        thing =splitinto(input("please state claims"))
        if checkClaim(thing , originalResources ,i):
            while len(thing) < len(numResources):
                print("skipped a resource please input zero")
                thing =splitinto(input("please state claims")) 
            if len(thing) > len(numResources):
                return " cant be done"
            matrix.append(thing)
    return matrix
def checkClaim(resourceClaim, originalResources, process ):

    for j in range(len(resourceClaim)):
        if resourceClaim[j] > originalResources[j]:
            print("No DEAL TOO GREEDY")
            print("process " , process , " wants resource",  resourceClaim[j] , " but maxcreated " , originalResources[j] )
            return False
    return True
    
allocatematrix = allocate(numResources, numProcs)

claimmatrix = claim(numProcs, numResources)

print("claimMatrix", claimmatrix)
print("allocationMatrix",allocatematrix)
print("resources left" , numResources)




def greenlight(claims , allocate , numRecs ):

    acopy = numRecs.copy()
    #print(claims , allocate , numRecs, " hahahahaha")
    value = sum(claims)
    #print(value)
    if value != 0:
        for j in range( len(claims)):
            acopy[j]+= allocate[j]
            #print(allocate[i], numRecs[i], claims[i],  " we here now ")
            if allocate[j] + numRecs[j] < claims[j] : 
                return False
    else:
        return False
    return acopy
def do(claimmatrix,allocatematrix, numResources ):
    for i in range(len(allocatematrix)):
        if greenlight(claimmatrix[i] , allocatematrix[i], numResources):
        
            claimcopy = claimmatrix.copy()
            allocatecopy = allocatematrix.copy()
            claimcopy[i] = [0] * len(claimcopy[i])
            allocatecopy[i] = [0] * len(claimcopy[i])
            numResourcesCopy = greenlight(claimmatrix[i] , allocatematrix[i], numResources)
            queue = deque()
            route= [i]
            queue.append((claimcopy, allocatecopy , numResourcesCopy, route))
            notfound = True
            while queue and notfound:
                claimvals , allocatevals, numResourcescopy2 , route = queue.popleft()
                # print("cur route" ,route)
                # print("cur resources" , numResourcescopy2)
                if len(route) == len(allocatematrix):
                    notfound = True
                    return route
                    
                for j in range(len(allocatevals)):
                    if greenlight(claimvals[j] , allocatevals[j], numResourcescopy2):
                        c_copy2 = claimvals.copy()
                        a_copy = allocatevals.copy()
                        c_copy2[j] = [0]* len(claimcopy[j])
                        a_copy[j] = [0]* len(claimcopy[j])
                        numrec_Copy = greenlight(claimvals[j] , allocatevals[j], numResourcescopy2)
                        routecopy = route.copy()
                        routecopy.append(j)
                        #print(routecopy , " haahaha")
                        queue.append((c_copy2,a_copy,numrec_Copy,routecopy))
    return "no safe state :("
print(do(claimmatrix, allocatematrix , numResources))
# for i in range(len(allocatematrix)):
#     if greenlight(claimmatrix[i] , allocatematrix[i], numResources):
        
#         claimcopy = claimmatrix.copy()
#         allocatecopy = allocatematrix.copy()
#         claimcopy[i] = [0] * len(claimcopy[i])
#         allocatecopy[i] = [0] * len(claimcopy[i])
#         numResourcesCopy = greenlight(claimmatrix[i] , allocatematrix[i], numResources)
#         queue = deque()
#         route= [i]
#         queue.append((claimcopy, allocatecopy , numResourcesCopy, route))
#         notfound = True
#         while queue and notfound:
#             claimvals , allocatevals, numResourcescopy2 , route = queue.popleft()
#             if len(route) == numProcs:
#                 print("route found" , route)
#                 notfound = True
#                 break
#             for j in range(len(allocatevals)):
#                  if greenlight(claimvals[j] , allocatevals[i], numResourcescopy2):
#                      c_copy2 = claimvals.copy()
#                      a_copy = allocatevals.copy()
#                      c_copy2[j] = [0]* len(claimcopy[j])
#                      a_copy[j] = [0]* len(claimcopy[j])
#                      numrec_Copy = greenlight(claimvals[j] , allocatevals[i], numResourcescopy2)
#                      routecopy = route.copy()
#                      routecopy.append(j)
#                      queue.append((c_copy2,a_copy,numrec_Copy,routecopy))
