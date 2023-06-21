"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""
"""
initial solution was make an intial dictionary and keeping count of all the elements it has as values and the  letter as key and then go through the rest
making a temp object and checking if it is equal to any exisiting dicitonar, if yes add it to that list at the dioctionary index whre it is found. if not then its a new anagram and add it to the dictionary of anagrams where index is related to the index of the results array and values. this solution at the bottom
"""
"""
revisited instead of computing all the letters of a word as key and the number of times they occur as value and compare dictionaries a much simpler option is to first sort the word alphabetically and store that as the key. on the first pass we will not have encountered this sorted word so store it as the key and for the value its index which will be zero. then increment the indexcount by one and append the original word to the results list. for all future words check if its sorted version has been seen before, if yes then append to the results according to the index value stored in the dicitonary. if not then add to the dictionary storing the indexcount as value and then increment the index count by one. repeat.
"""
def groupAnagrams(strs):
        


        theobject = {}
        indexcount = 0
        results = []

        for i in range(len(strs)):
            
            currentkey = "".join(sorted(strs[i]))

            if currentkey not in theobject:
                theobject[currentkey] = indexcount
                results.append([strs[i]])
                indexcount+=1
            else:
                results[theobject[currentkey]].append(strs[i])
        
        return results

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
    
        objectofobjects={}
        number1 = {}
        count = 0
        if strs == [[""]]:
            return strs
        for i in range(len(strs[0])):
            number1[strs[0][i]] = 1 + number1.get(strs[0][i],0)
    
        results.append([strs[0]])
        objectofobjects[count] = number1
        count+=1
        for i in range(1, len(strs)):
        
            temp = {}
            for j in range( len(strs[i])):
                temp[strs[i][j]] = 1 + temp.get(strs[i][j],0)
        
            track = True
            for z,x in objectofobjects.items():
                if temp == x:
                    results[z].append(strs[i])
                    track = False
            if track:
                objectofobjects[count] = temp
                results.append([strs[i]])
                count+=1
        
        return results