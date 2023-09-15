"""
You have an array nums. We determine two functions to perform on nums. In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i - 1] · nums[i + 1] · ... · nums[n - 1]. (In other words, fi(nums) is the product of all array elements except the ithf.)
g(nums) = f0(nums) + f1(nums) + ... + fn-1(nums).
Using these two functions, calculate all values of f modulo the given m. Take these new values and add them together to get g. You should return the value of g modulo the given m.

Example

For nums = [1, 2, 3, 4] and m = 12, the output should be
solution(nums, m) = 2.

The array of the values of f is: [24, 12, 8, 6]. If we take all the elements modulo m, we get:
[0, 0, 8, 6]. The sum of those values is 8 + 6 = 14, making the answer 14 % 12 = 2.
"""

"""
this problem really got me. I had the right intuition . first attempt used runningproduct as prefix  and then going backwards would divide by whatever number is stoed at that index to get roduct of all numbers except self. then modulo that and modulo the final sum but for extremely large numbers this does not work. 

my second attempt was pretty much the answer where I would try to avoid the division and generation of large numbers by essentially saying another way to look at all product except self was that the current index would be all the number to the left of current number mnultiplied, multiplied by all the numbers of the right multiplied. got a timeout error on the last test case.

finally third one is the one that passed.essentially a more efficient computation of the second attempt where postfix and prefix were calculated in a single loop and result was finally calculated by multiplying the two values  moduo m and then moduolo m and addin it to the current value of reuslt. thus avoiding expensive operations.
"""

#first attempt
def solution(nums, m):
    
    cursum = 1
    #this is a prefix problem and then a postfix problem
    res = [0] * len(nums)
    for i in range(len(nums)):
        
        cursum *= nums[i]
        res[i] = cursum
    
    print(cursum)
    final = 0
    for  j in range(len(nums)-1,-1,-1):
        
        res[j] = (cursum / nums[j]) 
        
        res[j] = res[j] %m
        
        final+= res[j]
    
    
    return final % m


#second attempt
def solution(nums, m):
    
    prefix = [1] * (len(nums))    
    for i in range(1,len(nums)):
        # saying  product of self for all numbers left of current number is equal to product of all numbers to left of current number
        # multiplied by most immediate left number
        prefix[i] = prefix[i-1] * nums[i-1]
    
    
    runningsum = 1
    result = 0
    #same as above but for right
    for j in range(len(nums)-2,-1,-1):
        prefix[j+1] = (prefix[j+1] * runningsum) % m
        result+= prefix[j+1]
        runningsum *= nums[j+1]
    
    result += (prefix[0]* runningsum) % m
    
    return result % m

#third attempt
def solution(nums, m):
    n = len(nums)
    
    prefix = [1] * n
    postfix = [1] * n
    
  
    prefix_product = 1
    postfix_product = 1
    
    for i in range(n):
        prefix[i] = prefix_product % m
        prefix_product = (prefix_product * nums[i]) % m
        
        postfix[n - 1 - i] = postfix_product % m
        postfix_product = (postfix_product * nums[n - 1 - i]) % m
    
    result = 0    
    for i in range(n):
        result = (result + (prefix[i] * postfix[i] % m)) % m
        
    return result