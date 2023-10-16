"""
in a game there is a string direction of length n that consists of characters L and R  l denotes lef and r denotes right and there is a line segemnet of length 2 **n that extends [0 , 2**n] aplayer takes n turns. game proceeds as follows for "LRRLLL"

direction
center   number     direction   remaining segement
                                    [0,64]
32          1           L           [0,32]
16          2           R           [16,32]
24          3           R           [24,32]
28          4           L           [24,28]
26          5           L           [24,26]
25          6           L           [24,25]

the smallest centoer point is 16 and the value palces is 2, the next smaller center is 24 with a value of 3 , when the centers are 
ordered ascending thier values  are 2,3,6,5,4,1

complete the function in the editor brloe

constraints 1 <= n <= 10 ^5
thr string consists of L and R only
"""

def find_the_equation(n,sequence):

    number = 2 ** n
    low = 0
    high = number
   
    count = 1
    maps = {}
    for i  in sequence:
        mid = (low + high)//2
        maps[mid] = count
        if i == "L":
            high = mid
        else:
            low = mid
        count+=1
    print(maps)

    array= [0] * (count -1)
    counting = 0
    for i , x in maps.items():
        array[counting] = i
        counting+=1
    array.sort()
    print(array)
    results = [0] * len(array)

    for i in range (len(array)):
        results[i]= maps[array[i]]
    print(results)    
        
        
        



print(find_the_equation(6,"LRRLLL"))