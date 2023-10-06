"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
solution(st) = "abcdcba".
"""

"""
there was no trick I could think of and could only approach this by brute force where I make every possoible combination of possible palindromes by adding it to the end of the string as per the constraints - since the strings where no lonfer than 10 chars and handle every case.There are away cleaner two liner solutions now that i can see the answers but my approach was such
-handle even palindromes then treating the last char as the middle of the palindrome genreate possible strings by adding the reverse of the string up tot hte pointer then the pointer and then anything after it.
finally loop through all generated strings and check if it is a palindome accounting for odd and even length styrings. return shortest string that satisfies this condition.
"""




def solution(string):
    palindromes = []
    
    
    palindromes.append(string)

    def even(string):
        temp = string
        left = len(string) - 1
        while string[left] == string[-1]:
            left -= 1
            if left < 0:
                break
        temp += string[left + 1 :: -1]
        palindromes.append(temp)
    even(string)
    right = len(string)-1
    while right >=0:
       temp = string[:right:] + string[right] + string[right+1::] +string[right::-1]
       palindromes.append(temp)
       right-=1

    def determinePalindrome(string):
        
        if len(string) % 2 == 0:
            print(string[:len(string)//2:],string[len(string)-1:(len(string)//2)-1:-1])
            return string[:len(string)//2:] == string[len(string)-1:(len(string)//2)-1:-1]
        else:
            
            print(string[:(len(string)//2):] ,string[len(string)-1:(len(string)//2):-1])
            return string[:(len(string)//2):]==string[len(string)-1:(len(string)//2):-1]
    
    maxCount = len(string) * 2
    curstr = ""
    for i in palindromes:
        if determinePalindrome(i) and len(i) <=maxCount:
            curstr = i
            maxCount = len(curstr)
    
    return curstr