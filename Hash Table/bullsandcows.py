"""
you are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 

Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
"""

"""
My approach is as follows. because the length of both of the strings are the same size we will be able to make comparisons of each letter at the respective index of both strings. it will be something like loop through first string store count then loop through second string and make comparison. if index chars are the same you have a bull. decrement frequency. if  digit exists  butnot in correct place then increment cow. howver there is important case to consider where a cow can be a potential bull later on in the loop. by this point youi mayhave deremented the count in the object to zero and the bull never gets updated. as such the thing i did was as follows
have bull , cow and potential bull variables that keep track of digits in place. loop through secret one object is the count and the other is a potential count. loop through the guess. if a digit in guess is in the count and its at the same index as secret then this is a bull. decrement both objecrt frequency. if digit is in count but not at the same index then you increment both cow and potentialbull. decrement the frequency only inthe count object and not the potential object. at this point if a char count no longer exists in count object but it exists in the potential object , then that means char marked as a cow is in fact a bull. decrement potential bull and cow by one , increment bull by one and decrement tghe frequency of that char in potential.
"""
def getHint(secret, guess):
            bulls = 0
            cows = 0
            potentialbulls = 0
    
            count = {}
            potential = {}
            for i in range(len(secret)):
                count[secret[i]] = 1+count.get( secret[i],0)
                potential[secret[i]] = 1+potential.get(secret[i],0)
        
            for j in range(len(guess)):
                if guess[j] in count :
                    if guess[j] == secret[j]:
                        bulls+=1
                        count[guess[j]] -=1
                        potential[guess[j]]-=1
                        if count[guess[j]]==0:
                            del(count[guess[j]])
                        if potential[guess[j]] == 0:
                            del(potential[guess[j]])
                    else:
                        count[guess[j]] -=1
                        if count[guess[j]]==0:
                            del(count[guess[j]])
                        cows+=1
                        potentialbulls+=1
                else:
                    if potentialbulls >0 and guess[j] == secret[j]:
                        potentialbulls-=1
                        cows -=1
                        bulls+=1
                        potential[guess[j]]-=1
                        if potential[guess[j]] == 0:
                            del(potential[guess[j]])
            return f"{bulls}A{cows}B"