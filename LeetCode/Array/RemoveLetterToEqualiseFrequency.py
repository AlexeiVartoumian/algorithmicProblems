"""
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.
 

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
"""
"""
Be careful! this are alot of edge cases too handle here and the examples given do not consider them. consider the edge case where all letters are equal except one where that letter frequency is one. for example "cccd" or "abbcc". its no longer a case of keeping count of the largest seen frequency. i opted for a brute force solution. i know theres ony 26 letters being handles so use an array of 26 length and loop thorugh array adding the ord(char)-97 value into array. then make a new array of all values in that array greater than 1. then double loop over that final array being subtracting 1 from each value and being careful to handle 0 values in that array.
"""

class Solution:
    def equalFrequency(self, word: str) -> bool:

        
        letters = [0] * 26

        for i in word:
            letters[ord(i)-97]+=1
        
        actualletters= []
        for i in letters:
            if i != 0:
                actualletters.append(i)
        
        
        for i in range(len(actualletters)):
            cur = i
            actualletters[i] -=1
            equalsofar = True
            number = actualletters[i]
            for j in range(len(actualletters)):
                if number == 0:
                    number =actualletters[j]
                elif actualletters[j] != number and actualletters[j] != 0:
                    equalsofar = False
            if equalsofar:
                return True
            actualletters[i]+=1
        return False