
# check d distance ahead and 2*d distance ahead. lookup in set.
def beautifulTriplets(d, arr):
    
    length =len(arr)
    sets = set(arr)
    numtrips = 0
    
    for i in range(length -2):
        if arr[i]+d in sets and arr[i] + 2*d in sets :
            numtrips+=1
    return numtrips