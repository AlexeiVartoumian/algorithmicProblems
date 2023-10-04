"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
solution(inputArray) = false.

There are 6 possible arrangements for these strings:

["aba", "bbb", "bab"]
["aba", "bab", "bbb"]
["bbb", "aba", "bab"]
["bbb", "bab", "aba"]
["bab", "bbb", "aba"]
["bab", "aba", "bbb"]
None of these satisfy the condition of consecutive strings differing by 1 character, so the answer is false.

For inputArray = ["ab", "bb", "aa"], the output should be
solution(inputArray) = true.

It's possible to arrange these strings in a way that each consecutive pair of strings differ by 1 character (eg: "aa", "ab", "bb" or "bb", "ab", "aa"), so return true.
"""
"""
the only way I could figure a way to attempt this problem was to consider the fact that i need to implement some sort of backtracking where I look at every combination of the arraylist and compare every letter to every word to see if they match or not at that position. as such for every elemetn in the array permute the arraylist if the respective charcount is DOES NOT equal 1 , otherwise this current combination might be a poosible permutation such that the difference in consecutive characters is less than 1. my approach nearly passed i got 19 out of 21 test cases correct but i was missing something on the first pass,the code below implements my approach
"""

def solution(inputArray):
    
   
    def is_adjacent(s1, s2):
        diff_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
        return diff_count == 1

    def dfs(arrangement, remaining):
        if not remaining:
            return True

        last = arrangement[-1] if arrangement else ""
        for i in range(len(remaining)):
            if is_adjacent(last, remaining[i]):
                if dfs(arrangement + [remaining[i]], remaining[:i] + remaining[i + 1:]):
                    return True

        return False

    for i in range(len(inputArray)):
        if dfs([inputArray[i]], inputArray[:i] + inputArray[i + 1:]):
            return True

    return False

#below was 1st attempt got does not pass everything
def solution(inputArray):
    
    
    def backtrack(current,combo,count):
        
        if combo ==[]:
            return True
        elif count == len(inputArray):
            return False
        else:
            for j in range(len(combo)):
                
                chars = 0
                for x in range (len(current)):
                    if current[x] != combo[j][x]:
                        chars+=1
                    if chars > 1 or current == combo[j]:
                        return backtrack(current, combo[j+1::]+combo[:j+1:],count+1)
                return backtrack(combo[j],combo[j+1::],count)
    
    
    for i in range(len(inputArray)):
        
        current = inputArray[i]
        combo = inputArray[:i:] + inputArray[i+1::]
        
        if backtrack(current,combo,1):
            return True
    
    return False