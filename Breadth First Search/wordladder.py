"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

"""
my initial apprach which was to first construct an adjacency list where the key is a word and the values would be all the other words such that 
are one letter away from that word. I thought sets would be the way to go for this where I would subtract a given set from another , if that
length was 1 then the difference would be one. THIS DOES NOT HANDLE WORDS WITH TWO LETTERS!!! it also does not handle the order in which the 
letters appear. if I were to force this optionthe only thing i could think of was to loop through every caharcter of a given word and compare it with every cahracter of another word such that there is only one difference. this would obviously exceeed time limit as the length of the word grows.
as such the second approach was to forget maaking the graph. and to instead turn the wordlist into a set. if end word is not in this set
return 0. then do bfs where we attempt to construct the next closest word on the fly. we do this by looping through each character of the alphabet
and use string slicing to concatenate the new word. if this new word is in the set list bingo  add it tot the queue and add it tot a visited set
so as not to embark in a infinite loop. keep a track variable which increments every time length of queue is inititated basically bfs at that pooint.
"""

from collections import deque
from collections import defaultdict
def ladderLength(beginWord, endWord, wordList):
        
        theset = set(wordList)

        if endWord not in theset:
            return 0
        
        queue = deque()
        queue.append(beginWord)
        track = 1
        changeitup = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        visited.add(beginWord)
        while queue:
            traverse = len(queue)
            track+=1
            for x in range(traverse):
                current = queue.popleft()
                for i in range(len(current)):
                    for j in range(26):
                        newword = current[:i] + changeitup[j] + current[i+1::] 
                        if newword in theset and newword not in visited:
                            queue.append(newword)
                            visited.add(newword)
                            if newword == endWord:
                                return track
        return 0





def wrongladderLength(beginWord,endWord ,wordList):
        if endWord not in wordList:
            return 0
        
        setchars = defaultdict(set)
        wordList = [beginWord] + wordList
        
        for i in  wordList:
            setchars[i] = set(i)
        
        adjlist = defaultdict(list)
        for i in range(len(wordList)-1):

            for j in range(i+1,len(wordList)):
                if len(setchars[wordList[i]] - setchars[wordList[j]]) == 1 :
                    adjlist[wordList[i]].append(wordList[j])
                    adjlist[wordList[j]].append(wordList[i])
        
        queue = deque()
        queue.append(beginWord)
        track = 1
        visited = set()
        visited.add(beginWord)
        print(adjlist)
        while queue:
            traverse  = len(queue)
            track+=1
            for i in range(traverse):
                current = queue.popleft()
                visited.add(current)
                for j in range(len(adjlist[current])):
                    if adjlist[current][j] not in visited:
                        if adjlist[current][j] == endWord:
                            print(visited)
                            return track
                        queue.append(adjlist[current][j])
        return 0


