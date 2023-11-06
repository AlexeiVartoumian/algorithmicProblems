
"""
You are planning production for an order. You have a number of machines that each have a fixed number of days to produce an item. Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.

For example, you have to produce goal equal to 10 items. You have three machines that take machiens = [2,3,2]  days to produce an item. The following is a schedule of items produced:

Day Production  Count
2   2               2
3   1               3
4   2               5
6   3               8
8   2              10
It takes 8 days to produce 10 items using these machines.

Function Description

Complete the minimumTime function in the editor below. It should return an integer representing the minimum number of days required to complete the order.

minimumTime has the following parameter(s):

machines: an array of integers representing days to produce one item per machine
goal: an integer, the number of items required to complete the order
"""
"""
my approach is tosort the machines into ascending order with a value pair of days to frequency .
after this i will ask the question can i make goal objects at an arbirtraily large number of days? my apporach was to first find this large number
where I can make goal objects. if at the first pass this is possible then I can 
 halve the number of days and ask the qurestion again until its no longer possible 
to do so. otherwise the min goal of days is within those bounds.
its at this point where a secondqary bin search is done to find
the first instance where it is possible to get goal objects on a given day but not possbile to get goal objects with 
given day -1. return the binsearh day where mid is possible but mid -1 is not possible
"""
def minTime(machines, goal):
    
    theobject = {}
    for i in range(len(machines)):
        theobject[machines[i]] = 1 + theobject.get(machines[i],0)
    def compute(days):
        asum = 0
        for i,x in theobject.items():
            asum+= (days//i) * x
            if asum >= goal:
                break
        if asum >= goal:
            return True
        else:
            False
    flag = True
    days = 10 **6
    prev = days
    asum = compute(days)
    def findmin(low,high):
        
        while low <= high:
            mid = int((low + high)/2)
            numberofdays  =compute(mid)
            if numberofdays and not compute(mid-1):
                return mid
            if not numberofdays:
                low = mid+1
            else:
                high = mid-1
    while flag:
        if not asum: # if current days do not meet quota find the bounds
            prev = days
            days*=2
            asum= compute(days)
        else:
            flag = False
    if prev != days:
        #skip locatefirstfailure # days will be a large sum
        return findmin(prev,days)
    else:
        flag = True
        while flag:
            asum = compute(days)
            if asum:
                prev = days
                days = days//2
            else:
                flag = False
        return findmin(days,prev)
#print(minTime(machines,goal))
machines = "1386 95 2944 4740 3903 4224 2078 3145 4079 329 2735 510 335 138 1452 4439 4280 1886 416 778 2240 4381 3002 963 975 528 2001 4620 2575 3013 2578 312 3107 521 1403 3361 4744 3480 1505 174 3808 591 683 494 2080 3487 4932 1359 372 1699 3488 2612 2432 1489 4926 3406 3369 3278 4377 2295 1290 1954 2606 748 3827 4009 4108 4922 3840 1964 1448 2648 2555 3482 3141 4634 1968 4425 2345 2340 2475 832 1303 4906 3673 2580 3311 2041 858 2687 4335 2147 993 3292 4247 1171 3652 3354 1092 2492 1670 3891 1491 576 2373 983 1561 4340 1759 3905 3031 586 4737 685 491 4761 3265 154 1801 4122 4192 2487 2620 184 2130 1866 2706 782 1572 150 4625 3241 4040 2467 3816 2764 4801 376 3456 1560 633 1486 2145 369 3523 3987 129 1787 4140 3281 908 3332 767 4879 4867 2896 1745 3925 29 3316 4074 1005 1556 4465 3471 1723 2229 3272 3450 684 1183 4082 3521 4679 802 2043 3665 2282 181 4157 1914 2440 3840 4032 2319 58 3280 4063 3982 3308 3730 4407 665 1637 3872 487 3359 2452 3758 3160 4487 1292 3594 3007 2322 4395 1402 987 3029 2934 1495 4942 374 334 3974 2692 391 3605 3106 725 3264 1835 131 3928 3471 354 4415 3181 2805 4524 1340 2291 2168 4933 1650 4489 680 4403 1827 3708 2336 3321 1 2709 3654 326 1752 397 3930 4857 2473 2194 1691 2603 2473 161 4309 1887 3341 2113 1411 1033 756 4930 965 2405 4418 2996 3159 1245 3055 494 4565 4408 4555 4571 4733 1306 1319 15 1163 3791 3560 2853 2745 1032 4366 2053 4271 4058 518 2033 90 1273 1962 2407 29 1379 402 3187 2623 4809 32 3540 4216 4586 3110 3948 892 780 314 3406 4570 3873 1258 3666 1257 1975 2071 1879 1033 2588 3911 1122 3860 2224 4880 240 3602 282 3426 2577 90 4809 2468 657 4395 577 4604 1638 2708 1270 1395 3629 1494 4004 2294 2750 979 4364 980 2011 1951 4890 3132 2162 2113 4364 2401 2067 4645 2178 995 1086 1987 3462 1742 2733 390 2697 722 3097 318 2116 1725 1812 1119 370 913 2097 4734 1893 459 3036 3134 4943 1550 1599 4306 302 3665 302 2480 4659 2739 818 3120 4480 4902 4861 3528 1975 2957 198 442 4681 2009 1560 50 2921 9 1135 1165 1819 523 4299 1761 2072 2249 1066 2373 913 1367 1204 1923 4105 3373 1394 4936 3274 1254 4816 1600 4210 13 2041 242 3373 4953 1643 2645 4961 4130 3810 1779 4652 4460 4892 1723 1708 957 447 3972 3676 1651 2246 4132 23 3639 420 4649 1244 1587 1248 1805 1599 4641 3398 4971 4593 1392 2615 905 521 2776 2683 1524 3587 3926 3246 294 4883 3693 617 4910 1695 2862 393 3069 1500 812 2717 4095 2398 317 899 348 4957 4296 1670 901 688 4285 1805 1208 3412 839 4084 1999 4765 2329 3644 4647 2373 4261 908 419 2122 1300 3488 4974 2112 1204 4068 861 2872 1319 1209 4180 614 2878 80 1301 3514 1884 3861 3278 2723 2944 276 2487 1624 3919 3485 349 4531 4392 767 3005 2043 4254 2978 506 1810 3397 1367 4681 4715 3927 213 1681 1804 292 4333 1670 2176 4545 4947 4898 2488 1574 2384 464 492 2220 2164 1375 1611 2930 4379 3653 3536 2356 4159 1697 2104 1877 2729 3171 803 2941 4851 3958 3233 4183 1979 408 3728 1925 1657 2567 4850 392 3030 1694 2611 1545 3068 4221 4475 2446 4225 4362 1153 4735 2410 3256 2963 138 1426 117 3079 2628 4075 2663 1811 2405 4422 538 682 1078 4456 531 1469 2486 2224 431 4030 291 4651 4856 4088 227 569 240 1314 2978 4848 4276 3116 2625 4393 2546 253 4819 208 3415 2223 4629 304 2904 2058 4759 4787 4878 3596 2010 308 2626 3653 1310 3833 2740 2888 754 4332 4201 3731 531 3477 3198 4507 4221 2095 1111 4039 2302 4525 2613 3282 4828 517 1691 4587 1655 1568 3182 3664 3227 2159 2316 4536 2344 1408 2424 3097 2091 1624 3179 2621 1452 1377 3479 2024 4823 4590 1062 3477 4114 3675 1758 294 543 4801 4880 2197 2720 4413 2212 947 2924 880 482 267 3639 4257 4715 729 2233 4245 4701 36 1973 3179 2060 1796 2768 4473 272 3234 4499 3381 3527 1393 3181 4758 4941 901 522 2153 3199 3445 4384 32 63 3022 4289 1129 102 2873 374 4802 2908 2346 4332 1319 4141 3452 792 764 1685 290 4145 1563 1683 2325 2672 1623 4577 3193 127 2775 2990 4510 4159 3052 3883 3447 533 3984 2671 906 137 578 4603 4469 1897 3744 2920 4040 4507 956 4329 3 3870 2363 3680 1541 338 3256 4733 464 2383 2722 1326 1541 2126 208 1339 2658 4192 4009 4915 680 938 4517 148 4186 4612 4419 3225 471 1726 3906 473 595 2620 4152 2135 2957 3760 3220 4773 1142 2293 2450 4034 4418 2657 372 3427 3200 732 3341 3880 1669 2858 379 855 3821 4798 431 4291 2875 4336 1116 3470 1956 267 1956 1264 378 175 1036 1519 2468 3485 1904 3237 2494 3627 1664 693 4358 1356 924 1027 4213 1303 3233 4386 2452 3663 3676 326 2999 4791 147 1306 1410 2103 2569 1787 3629 3605 4658 2448 3441 1561 2037 934 188 3700 2979 897 1407 3902 1923 620 1556 1507 1357 359 170 32 2037 4520 1175 2183 825 3936 637 4745 2074 618 4701 1731 4417 3142 4644 1453 427 1183 1504 3405 2079 2911 3659 354 4882 1566 1860 2590 1925 3381 3973 313 2900 147 3847 76 434 836 4821 2508 1453 4521 590 2221 4014 1585 26 4441 4119 2881 4197 1198 2143 2855 2903 3376 4421 4762 965 2697 4495 4938 4361 2394 1436"

#goal = 844676607
#print(machines, len(machines))

machines =list( map(int , machines.split(" ")))
