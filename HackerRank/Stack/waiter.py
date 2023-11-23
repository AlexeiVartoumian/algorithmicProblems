"""
You are a waiter at a party. There is a pile of numbered plates. Create an empty answers array. At each iteration, i, remove each plate from the top of the stack in order. Determine if the number on the plate is evenly divisible by the ith prime number. If it is, stack it in pile Bi . Otherwise, stack it in stack Ai. Store the values in Bi from top to bottom in answers. In the next iteration, do the same with the values in stack Ai. Once the required number of iterations is complete, store the remaining values in  Ai in answrs, again from top to bottom. Return the answers array.

Example:
A = [2,3,4,5,6,7]
q = 3
an abrreviated list of primes i s [2,3,5,7,11,13].
stack the plates in reverse order
A0 = [2,3,4,5,6,7]
answers =[]
Begin iterations. On the first iteration, check if items are divisible by 2.
A1 = [7,5,3]
B1 = [6,4,2]
Move B1 elements to Answers
answers =[2,4,6]

On the second iteration, test if  A1 elements are divisible by 3.
A2 = [7,5]
B2 = [3]
Move B2 elements to answers.
Answers = [2,4,6,3]

And on the third iteration, test if A2 elements are divisible by 5.
A3 = [7]
B3 = [5]
Move B2 elements to Answers.
Answers = [2,4,6,3,5]

All iterations are complete, so move the remaining elements in A3, from top to bottom, to answers.

Answers = [2,4,6,3,5,7]
. Return this list.

Constraints:
1 < n <= 5 * 10^4
2<=number[i] <= 10 ^ 4
1<=q<=1200
"""
"""
this is a stack question. first I need to generate the primes since in constraints q will be no larger than 1200 I could use erasthenos seive where I starting from 2 I ask are any numbers up to range divisible by cur number. if so not a prime.
otherwise if i havent encountered it before its a prime.
after that its a question of going through those primes and applying the procedure
where if cur number % 2 == 0 it will eventually go to my answers array.
otherwise it will go to the other bucket for further processing. on each pass of array pop the matching numbers into the answers and the 
other stack is processed with consequent
primes. one last check that numbers still exists in the orginal array.
"""


def waiter(number, q):
    # Write your code here
    
    primes = [2]
    
    answers = []
    count = 1
    notprimes = set()
    notprimes.add(2)
    if count != q:
        for i in range(2,9734):
            if i not in notprimes :
                count+=1
                primes.append(i)
                if count == q:
                    break
            for j in range(i,9734,i):
                notprimes.add(j)
    for prime in primes:
        stackA= []
        stackB = []
        while number:
            num = number.pop()
            if num % prime == 0:
                stackA.append(num)
            else:
                stackB.append(num)
        while stackA:
            answers.append(stackA.pop())
        number = stackB
    while  number:
        answers.append(number.pop())
    return answers