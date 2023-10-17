
"""
I failed this question. my approachwas to for every number check the second number and third number if they are in the 
dicitonary and if so store the count that they have in variables. if its possible to make a triplet then the number of possible triplets would be freq * varible1 * vairbale2 where the variables are frequency of the second and third number in a geometric progression.but this does not consider all test cases for example where there is only 1 digit of which there issay 100000 frequency and r = 1. as such I looked online and saw this solution and its beautiful and simple at the same time.
it basically works backwards and asks is this number a possible 3rd number in a geometric sequence? is so then add to the count all pair combinations frequency which have been seen. this backwards approach and the brilliant part is acheived by curnumber*(r * r) to get the third number and i% r to get the second number. at every pass add the current number to the frequency which in turn is the number that gets added to the pair frequency whenever second number occurs.
"""
astring  = "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1"

arr = list(map(int ,astring.split(" ")))
#below is the my understanding of this solution and below was my attempt it passed half of the tests.
from collections import defaultdict
def countTriplets(arr, r):
    
    freqs = defaultdict(int)
    pairs_before_poss_triplets = defaultdict(int)
    count = 0
    for i in arr:
        #beautiful way of asking is this my third number
        #if so add the frequency pairs to my count
        if i % (r*r) == 0:
            # even more beautiful way more of saying
            #add all the pair combos seen up until that point
            count+= pairs_before_poss_triplets[i //r]
        if i % r == 0: #is this the second number in the geometric sequence
            #then add all first numbers in my geometric sequence
            pairs_before_poss_triplets[i] += freqs[i//r]
        freqs[i]+= 1
    
    return count
def countTriplets(arr, r):
    arr.sort()
    freqs = {}
    for i in arr:
        freqs[i]=  1 + freqs.get(i,0)
    
    print(freqs)
    total = 0
    for curnumber, frequency in freqs.items():
        temp1 =0
        temp2 = 0
        count = 1
        flag = True
        shift = curnumber
        while count < 3 and flag:
            if shift*r in freqs:
                 shift*=r
                 count +=1
                 #temp += freqs[shift]
                 
                 if count == 2:
                     temp1 = freqs[shift]
                 else:
                     temp2 = freqs[shift]
            else:
                flag = False
        if flag:
            #total += frequency * temp
            total += frequency * temp1 * temp2
    return total
print(countTriplets(arr,1))
166661666700000


161700