"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

 

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
"""


from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict = {}
        for word in words:
            if word in dict: dict[word] = dict[word] + 1
            else: dict[word] = 1

        array = []
        for key in dict:
            value = dict[key]
            array.append((-value, key))

        def apply(x):
            (_, key) = x
            return key
        
        array.sort()

        return list(map(apply, array))[0:k]


def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        cnt = Counter(words)
        
        print(cnt.items())
        
        most_list = sorted(list(cnt.items()), key=lambda x: [-x[1], x[0]])
        
        print(most_list)
        
        answer = []
        
        for i in range(k):
            answer.append(most_list[i][0])
            
        return answer