"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
"""
My approach seems to work but is also not efficient. the way I approached this is as follows. step1: keep count of all characters in p with char as key and frequency as val.
step 2. have a second dictionary and use this to keep track of characters in s, index is key and value is the p object. the idea is using p dictionary as value , decrement the value by one whenever a character in there appears , if the sum of the entire object equals zero then an anagram is here and delete that key from s dictionary - sub process in step 3
step3: case 1: a unique index in s is not in s dictionary but  s at that index is in p dictionary ; means its the start of a potential anagram
        subprocess: step 1: if s dictionary not empty loop through all indexes value objects and decrement current char key by one
        step2:if this value becomes -1 then current substring is not an anagram, same letter has appeared more times than in p string, make note of index  and store in array to be deleted from s dictionary later on 
        step3: if the stored array is empty and the total value of the index object is zero then its an anagram! append the index to results array
        and then delete that index from the s dictionary.

        move to the next element
        
        case 3: current element in s is not in p 
        that means all current key value pairs in dictionary cannot be anagrams . the task is to delete all key value pairs and start over

        move to the next element

The problem with this is that it requires constant checking and looping through the dictionaries and updating. The way more effiecient approach is to use the sliding window technqiue with two dictionaries like above but with the following procedure.

step 1: loop through the smaller substring p and and update two dictionaries. one will keep track of s and the other will keep track of p. in each will be stored the character as the key , and the frequency as value. 

step2. IN PYTHON YOU CAN USE THE EQUALITY OPERATOR TO CHECK IF BOTH DICTIONARIES ARE THE SAME. IF SO THEN ADD 0 INDEX AS AN ANAGRAM TO THE RESULTS ARRAY. THIS IN COMBINATION WITH SLIDING WINDOW BELOW IS HOW WE CHECK IF EVERY SUBSTRING IS AN ANAGRAM OR NOT.

step3. at this point we  can intialise the sliding window technique here is the subprocess.
    step1: instantiate a left pointer to 0
    step2: loop through the s string only this time start at position of length p string as you already looped in previous step up to this point. the trick here is that the index of this loop will be used as the right pointer of the sliding window.

    step3: update the s dictioanary value at the index of the new loop incrementing it by 1. this is the act of slding right of the string
    step4: decrement the index of s dictionary at position leftpointer by one. if this key value pair reaches zero it means we have moved left enough such that that character no longer exists in the substring and we can now pop that key value pair from the s dicitonary. In other words slide the window to the left and see if current element still exists in new substring

    step5: SLIDE THE WINDOW!  increment leftpointer by one

    step6: finally check if the current substring is equal to the dictionary of p in other words can you make an anagram of the current substring into the string p.
"""

def findAnagrams(s, p):

        if len(p) > len(s):
            return []
        
        elif len(p) == 1:
            res = []
            for i in range(len(s)):
                if s[i] == p[0]:
                    res.append(i)
            return res
        theobject = {}
        change = {}
        res = []
        
        for i in range(len(p)):
            if p[i] not in theobject:
                theobject[p[i]] = 1
            else:
                theobject[p[i]]+=1
      
        for i in range(len(s)):
            if i not in change and s[i] in p:
                
                tracker = []
                for k,v in change.items():
                    
                    
                    change[k][s[i]] -=1
                    if change[k][s[i]] == -1:
                        tracker.append(k)
                    
                    
                    
                    if sum(v.values()) == 0 and tracker == []:
                            tracker.append(k)
                            res.append(k)
                for j in tracker:
                    del change[j]
                
                change[i] = theobject.copy()
                
                change[i][s[i]] -=1
            elif s[i] not in p :
                deletekeys = []
                for k,v in change.items():
                    deletekeys.append(k)
                
                for j in deletekeys:
                    del change[j]
        return res




def findanagrams(s,p):
    if len(p)> len(s):
        return []
    
    theobject = {}
    sliding = {}
    # loop through string p and add respective characters in both strings
    # s and p to respective dictionaries
    for i in range(len(p)):
        theobject[p[i]] = 1 + theobject.get(p[i],0 ) # get allows us to instantiate a new occurence of a key with a default value of zero if it does no exist else will deliver the value
        sliding[s[i]] = 1+ sliding.get(s[i],0)
    #at the end of loop we will have two dictionaries of same length as p 
    res = [] 
    if theobject == sliding:
        res= [0]
    
    leftpoint = 0 # this represents the left part of our left part of sliding window
    
    #i will start at substring p and finish at length s acts as right part of sliding window
    for i in range(len(p), len(s)):
        #step1 using i as right pointer move along string s and decrement amount of values in at position leftpoint
        sliding[s[i]]=  1 + sliding.get(s[i],0) #move to the right
        sliding[s[leftpoint]] -=1 #slide away to next element
        if sliding[s[leftpoint]] == 0:# if this is zero that means in current substring that means we have moved left enough times where its no longer part of substring
            sliding.pop(s[leftpoint])
        leftpoint+=1 #update lefpoint of window to current substring 
        if theobject == sliding: # check if they are equal
            res.append(leftpoint)
    

