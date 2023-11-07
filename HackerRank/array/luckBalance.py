"""
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is described by two integers, L[i] and T[i] :

 L[i]is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; if she loses it, her luck balance will increase by L[i] .
 T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.
If Lena loses no more than  important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? This value may be negative.

Example



Contest		L[i]	T[i]
1		5	1
2		1	1
3		4	0
if Lena loses all of the contests, her will be 5 + 1 + 4 = 10. Since she is allowed to lose 2 important contests, and there are only 2 important contests, she can lose all three contests to maximize her luck at .

If k= 1, she has to win at least 1 of the 2 important contests. She would choose to win the lowest value important contest worth 1. Her final luck will be 5 + 4 -1 = 8
"""

"""
I apporached this by sorting the entire array with lambdas using the second index of the to denote the important constests and non important contests.
I did this because I then wanted to partition this now sorted list into the two groups where I can then again use lambda to sort the lists according to 
the value of the contest. after that its a case of adding up all the luck in the non important group and subtracting all values in the important group 
that appear within the bounds of length important list minus k ; which is the number of contests lena has to win since k is the number of important contests she can lose and adding the luck of all important contests that appear after  length important list minus k.
"""

def luckbalance(k, contests):
    # Write your code here
    contests.sort(key = lambda i : i[1])
    canlose = []
    important =[]
    
    
    for i in range(0,len(contests)):
        
        if contests[i][1] == 0:
            canlose.append(contests[i])
        else:
            important.append(contests[i])
        
    canlose.sort( key = lambda i : i[0])
    important.sort( key = lambda i :i[0])
    luck = 0
    
    for i in range(len(canlose)):
        luck += canlose[i][0]
    count = len(important) - k
    for i in range(len(important)):
        if i  < count:
            luck-= important[i][0]
        else:
            luck+= important[i][0]
    return luck



contests = """5351 0
1870 0
9359 0
6828 0
9896 0
6335 0
38 0
2440 0
4627 0
2663 0
6300 0
107 0
4605 0
5437 0
4394 0
7530 0
8254 0
5668 0
6945 0
1539 0
1323 0
1841 0
2191 0
8943 0
7645 0
3903 0
4772 0
2392 0
1539 0
7712 0
9955 0
9895 0
7422 0
4665 0
5448 0
2317 0
6963 0
9170 0
2860 0
3812 0
5725 0
1324 0
7377 0
5538 0
2383 0
7674 0
5142 0
3932 0
2624 0
8704 0
5706 0
2649 0
6730 0
8757 0
2930 0
4465 0
6119 0
4967 0
8717 0
334 0
9962 0
293 0
1943 0
8146 0
4085 0
779 0
9630 0
1843 0
289 0
2083 0
9742 0
5891 0
2996 0
7447 0
4371 0
1102 0
6501 0
492 0
3806 0
3549 0
9719 0
9913 0
9265 0
8468 0
5007 0
1479 0
2758 0
1727 0
5548 0
6869 0
154 0
42 0
6309 0
9041 0
3036 0
3282 0
4828 0
7036 0
8724 0"""

contests = """5 1
2 1
1 1
8 1
10 0
5 0"""


#contests = list( map( int , contests.split(" ")))

contests = contests.splitlines()
#print(contests)



contests =  list ( list(map(int , x.split(" "))) for x in contests )  
#print(contests, len(contests))
k =3
