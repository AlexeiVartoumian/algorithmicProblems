"""
ab
bb
hefg
dhck
dkhc
"""

"""
ba
no answer
hegf
dhkc
hcdk
"""



# def permutations(word , combos , combo , seen):

    
#     for i in range(len(word)):
        
#         print(combo)
#         if len(combo) == len(word):
#             if combo not in seen:
#                 seen.add(combo)
#                 combos.append(combo)
#                 return combos
        
#         permutations(word , combos , combo+ word[i:i+1] , seen)       
        

    
#     return combos

    

# print(permutations("abc" , [], "" , set()))

# print([ord(i) for i in list("dkhc") ])

# "yitveovrja"

# print([ord(i) for i in list("yitveovrja") ])
# print([ord(i) for i in list("yitverajov") ])
# print([ord(i) for i in list("pnimbesirfbivxl") ])

## the problem is such . its a sliding window problem where the goal is to answer the question
## how close can ig et to the end of the word where the left pointer is closest to the end of the string and the right pointer is larger than it?

from collections import defaultdict
def slidingWindow(word):

    leftpointer = None
    rightpointer = None

    book = defaultdict(int)
    for i in range(len(word)-1):
    
        for j in range(i+1 ,len(word)):
            if ord(word[i]) < ord(word[j]):
                leftpointer = i
                rightpointer = j
    if leftpointer == None or rightpointer == None :
        return "no answer"
    #print(leftpointer , rightpointer)
    word = word[:leftpointer:] + word[rightpointer:rightpointer+1:] + word[leftpointer+1:rightpointer:] + word[leftpointer:leftpointer+1:] + word[rightpointer+1::]
    #print(word)
    for k in range(leftpointer+1 , len(word)):
        book[ord(word[k])] +=1
    answer = word[:leftpointer+1:]
    for z in range(97 , 123):
        if z in book:
            answer = answer + chr(z) * book[z]

    return answer

        
print(slidingWindow("dkhc"))
print(slidingWindow("yitveovrja"))


def slidingwindow(word):

     
    leftpointer = None
    for i in range(len(word)-2, -1, -1):  
        if ord(word[i]) < ord(word[i+1]):
            leftpointer = i
            break  
    
    if leftpointer is None:
        return "no answer"
    
    
    rightpointer = None
    for j in range(len(word)-1, leftpointer, -1):  
        if ord(word[j]) > ord(word[leftpointer]):
            rightpointer = j
            break  
    
    chars = list(word)
    chars[leftpointer], chars[rightpointer] = chars[rightpointer], chars[leftpointer]
    
    
    chars[leftpointer+1:] = sorted(chars[leftpointer+1:])
    
    return ''.join(chars)



def timeInWords(h, m):
    # Write your code here
    minutes= {
        0: "o' clock",
        15: "quarter past ",
        30: "half past ",
        45: "quarter to ",
    }
    hours= {1 : "one" , 2: "two", 3: "three"  ,4 :"four" ,5: "five" ,6:"six" ,
        7:"seven",8: "eight" ,9: "nine" ,10: "ten" ,11:"eleven" ,12 : "twelve" , 13: "thirteen",
        14 :"fourteen" , 15: "fifteen"
    }
    
    if m in minutes :
        
    
        if m == 45 and h != 12:
            
            return minutes[m] + hours[h+1]
        elif h == 12 and m ==45 : 
            return minutes[m] + hours[1]
        if m == 15:
            return minutes[m] + hours[h]
        if m == 30:
            return minutes[m] + hours[h]
        if m == 0:
            return hours[h]+ " " + minutes[m] 
        
        
    
    if m >= 10 :
        first , second = int(str(m)[0]) , int(str(m)[1])
    
    if m == 1:
        return hours[m] + " minute past " + hours[hours]
    if m <= 13:
        return hours[m] + " minutes past " + hours[hours]
    if m <20:
        return hours[m]+ "teen" + "minutes past " + hours[h]
    if m < 30 :
        return "twenty "+ hours[second] +" minutes past " + hours[h]
    if m >30 and m < 45 :
        if h == 12:
            return "twenty "+ hours[second] +" minutes to " + hours[1]
        return "twenty "+ hours[second] +" minutes to " + hours[h+1]
    else:
        if h == 12:
            return hours[60 - m] + " minutes to " + hours[1]
        return hours[60 - m] + " minutes to " + hours[h+1]
    
    
    
print(timeInWords(1 , 1) )