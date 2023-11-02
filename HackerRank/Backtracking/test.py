arr2 = ['CANADA','TELAVIV','NIGERIA','ALASKA','LASVEGAS','CALIFORNIA']
string = "CALIFORNIA;LASVEGAS;NIGERIA;CANADA;TELAVIV;ALASKA"

arr = string.split(";")

print(arr)
"""
newarray = []
permutations = []
def backtrack(start,arr,arrcopy):

    if len(arrcopy) == len(arr):
        permutations.append(arrcopy.copy())
        return
    for i in range(start,len(arr)):
        arr[i],arr[start] = arr[start],arr[i]
        arrcopy.append(arr[start])
        backtrack(start+1,arr,arrcopy)
        arr[start],arr[i] = arr[i],arr[start]
        arrcopy.pop()
backtrack(0,arr,[])
print(permutations,len(permutations))

if arr2 in permutations:
    print(arr2, "ahahahah")
"""

permutations = set()
def backtrack(start,arr,arrcopy):

    if len(arrcopy) == len(arr):
        permutations.add(tuple(arrcopy.copy()))
        return
    for i in range(start,len(arr)):
        arr[i],arr[start] = arr[start],arr[i]
        arrcopy.append(arr[start])
        backtrack(start+1,arr,arrcopy)
        arr[start],arr[i] = arr[i],arr[start]
        arrcopy.pop()
backtrack(0,arr,[])

permutations = [list(perms) for perms in permutations]
print(permutations,len(permutations))
if arr2 in permutations:
    print(arr2, "ahahahah")





