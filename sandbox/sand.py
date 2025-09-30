

# import math
# import os
# import random
# import re
# import sys
# from collections import defaultdict
# #
# # Complete the 'biggerIsGreater' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING w as parameter.
# #

# def biggerIsGreater(w):
#     book = defaultdict(int)
#     stringer = ""
#     curchar = ""
#     stop = False
#     seen = set()
#     for i in range(len(w)-1 , -1 , -1):
         
        
#         curchar = w[i]
                     
#         for j in range(i-1 , -1 , -1 ):
               
#             if ord(w[i]) > ord(w[j]):
                     
#                 stringer = w[:j] + w[i]
                
#                 stop = True
#                 book[ord(w[j])]+=1
#                 for z in range(j+1 , len(w)):
#                     #print(w[z])
#                     if z != i:
#                         book[ord(w[z])] += 1
#                 break
        
#         if stop :
#             break 
#         book = defaultdict(int)
#         seen = set()
    
#     if stringer == "":
#         return "no answer"
    
#     #print(book)
#     for i in range(97 , 123):
        
#         if i in book :
#             stringer = stringer + (chr(i) *book[i]) 
    
#     return stringer



thing = """
imllmmcslslkyoegymoa
fvincndjrurfh
rtglgzzqxnuflitnlyit
mhtvaqofxtyrz
zalqxykemvzzgaka
wjjulziszbqqdcpdnhdo
japjbvjlxzkgietkm
jqczvgqywydkunmjw
ehdegnmorgafrjxvksc
tydwixlwghlmqo
wddnwjneaxbwhwamr
pnimbesirfbivxl
mijamkzpiiniveik
qxtwpdpwexuej
qtcshorwyck
xoojiggdcyjrupr
vcjmvngcdyabcmjz
xildrrhpca
rrcntnbqchsfhvijh
kmotatmrabtcomu
bnfcejmyotvw
dnppdkpywiaxddoqx
tmowsxkrodmkkra
jfkaehlegohwggf
ttylsiegnttymtyx
kyetllczuyibdkwyihrq
xdhqbvlbtmmtshefjf
kpdpzzohihzwgdfzgb
kuywptftapaa
qfqpegznnyludrv
ufwogufbzaboaepslikq
jfejqapjvbdcxtkry
sypjbvatgidyxodd
wdpfyqjcpcn
baabpjckkytudr
uvwurzjyzbhcqmrypraq
kvtwtmqygksbim
ivsjycnooeodwpt
zqyxjnnitzawipqsm
blmrzavodtfzyepz
bmqlhqndacv
phvauobwkrcfwdecsd
vpygyqubqywkndhpzw
yikanhdrjxw
vnpblfxmvwkflqobrk
pserilwzxwyorldsxksl
qymbqaehnyzhfqpqprpl
fcakwzuqlzglnibqmkd
jkscckttaeifiksgkmxx
dkbllravwnhhfjjrce
imzsyrykfvjt
tvogoocldlukwfcajvix
cvnagtypozljpragvlj
hwcmacxvmus
rhrzcpprqccf
clppxvwtaktchqrdif
qwusnlldnolhq
yitveovrja
arciyxaxtvmfgquwb
pzbxvxdjuuvuv
nxfowilpdxwlpt
swzsaynxbytytqtq
qyrogefleeyt
iotjgthvslvmjpcchhuf
knfpyjtzfq
tmtbfayantmwk
asxwzygngwn
rmwiwrurubt
bhmpfwhgqfcqfldlhs
yhbidtewpgp
jwwbeuiklpodvzii
anjhprmkwibe
lpwhqaebmr
dunecynelymcpyonjq
hblfldireuivzekegit
uryygzpwifrricwvge
kzuhaysegaxtwqtvx
kvarmrbpoxxujhvgpw
hanhaggqzdpunkugzmhq
gnwqwsylqeuqr
qzkjbnyvclrkmdtc
argsnaqbquv
obbnlkoaklcx
ojiilqieycsasvqosycu
qhlgiwsmtxbffjsxt
vvrvnmndeogyp
ibeqzyeuvfzb
sajpyegttujxyx
zmdjphzogfldlkgbchnt
tbanvjmwirxx
gmdhdlmopzyvddeqyjja
yxvmvedubzcpd
soygdzhbckfuk
gkbekyrhcwc
wevzqpnqwtpfu
rbobquotbysufwqjeo
bpgqfwoyntuhkvwo
schtabphairewhfmp
rlmrahlisggguykeu
fjtfrmlqvsekq
"""

# thing = """
# ehdegnmorgafrjxvksc
# """


# print(chr(109))




#fuck = "bivxl"

# fuck = "dkhc"

print( [ord(i) for i in list("yitveovrja")])
from collections import defaultdict

def biggerIsGreater(w):
    book = defaultdict(int)
    answer = "yitverajov"
    fucks = []
    stop = False
    for i in range(len(w)-1 , -1 , -1):  
        curchar = w[i]
                     
        for j in range(i-1 , -1 , -1 ):
            if ord(w[i]) > ord(w[j]):
                stringer = w[:j] + w[i]
                
                leftpointer = j+1
                rightpointer = i-1
                book[ord(w[j])]+=1
                for z in range(j+1 , len(w)):
                    if z != i:
                        book[ord(w[z])] += 1
                for i in range(97 , 123):
                    if i in book :
                        stringer = stringer + (chr(i) *book[i]) 
                        fucks.append(stringer)
                stop = True
                
                while leftpointer < rightpointer :
                    book = defaultdict(int)
                    for k in range( rightpointer , leftpointer, -1):
                        
                        if ord(w[k]) > ord(w[leftpointer]):

                            stringer = w[:leftpointer] + w[k]
                            #print("answer is" ,answer)            
                            #print(stringer , "is now" , leftpointer ,w[leftpointer], w[rightpointer],rightpointer , k)
                            book[ord(w[leftpointer])]+=1
                            for z in range(k+1 , len(w)):
                                if z != k:
                                    book[ord(w[z])] += 1
                            for i in range(97 , 123):
                                if i in book :
                                    stringer = stringer + (chr(i) *book[i]) 
                            fucks.append(stringer)
                    #rightpointer = k
                    leftpointer+=1
                if stop :
                    break
        if stop :
            break
        book = defaultdict(int)
    
    if not fucks :
        return "no answer"
    #print(fucks)
    
    return fucks[-1]


biggerIsGreater("yitveovrja")


# for i in thing.splitlines():
#     #print(i.strip())
#     print(biggerIsGreater(i.strip()))
#     #print(" ")