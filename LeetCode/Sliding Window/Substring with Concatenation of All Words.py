"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
The output order does not matter. Returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
We return an empty array.
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
"""
"""
in the words of uncle roger "HIYAAAAAAAAAAAAAAAAAA"
seriously though this problem really got me going with the edge cases.
in the end the solution i came up with was this.
an unoptimised sliding window within a sliding window.
the outer sliding window will always be the length of all letters in words list.
the inner sliding window will compute if a current outer window is actually a 
substring with concatenation. here i am pedantic. if at any point this is not the case then left pointer shifts by one and not by length of word. then a new outer window is made and the process repeats.
"""



class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res =[]
        windowlength = len(words[0]) * len(words)
        letters = set()
        original= {}
        window = {}
        step = len(words[0])
        for i in words:
            original[i] = 1 + original.get(i,0)
            letters.add(i[0])
        left = 0
        curstr =""
        track =0
        for r in range(len(s)):
            if r-left+1 != windowlength:
                continue
            else:
                for innerleft in range(left,r+1):
                    curstr+=s[innerleft]
                    track+=1
                    if track == step:
                        if curstr not in original:
                            start = left
                            while left < r+1 and s[left] not in letters:
                                left+=1
                            curstr= ""
                            track = 0
                            window ={}
                            if start == left:
                                left+=1
                            break    
                        else:
                            window[curstr]= 1+window.get(curstr,0)
                            if window == original:
                                res.append(left)
                                curstr = ""
                                track =0
                                left+=1 #make new window
                                window = {}
                                break
                            elif window[curstr] > original[curstr]:
                                left+=1
                                window = {}
                                curstr= ""
                                track =0
                                break
                            else:
                                curstr= ""
                                track = 0
        return res