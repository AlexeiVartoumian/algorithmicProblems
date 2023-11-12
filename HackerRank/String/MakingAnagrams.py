"""
A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.

Given two strings,a and b, that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams.Any characters can be deleted from either of the strings.

Example 
a = 'cde'
b = 'dcf'
Delete  e from  a and f from  b so that the remaining strings are cd and dc which are anagrams. This takes 2 character deletions.
"""
"""
used two arrays of length 26 to represent the letters of each string. input states they will be lowercase. loop through smaller
array adding char count with ord() function for both strings. complete for greater length if exists. finally the number of deletions needed will be the sum of absolute differences at every index between the two letter counts. 
"""
def makeAnagram(a, b):
    # Write your code here
    
    lettersa = [0] * 26
    lettersb = [0] * 26
    length = min(len(a),len(b))
    greater = max(len(a),len(b))
    def restof(length, greater, string,arr):        
        for i in range(length, greater):
            letter=  ord(string[i])-97
            arr[letter]+=1
        return arr
    for i in range(length):
        lettera,letterb =  ord(a[i])-97 , ord(b[i])-97
        lettersa[lettera]+=1
        lettersb[letterb]+=1
    
    if len(a) > len(b):
        restof(length,greater,a ,lettersa)
    elif len(b)> len(a):
        restof(length,greater,b,lettersb)
    
    total= 0
    for i in range(26):
        total += abs(lettersa[i] - lettersb[i])
    
    return total