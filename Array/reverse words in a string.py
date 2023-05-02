"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
s does not contain any leading or trailing spaces.
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""

"""
the approach i used only works because s does not have any leading spaces or trails.
the idea was to turn split the string into an array and then iterate over each element starting at the last element and appending it to the new string. after this is inner loop is done the idea is to add a space add keep repeating until finished.
one thng to watch out for though is since there are not leading spaces in the string and we are reversing it you will need to return the reverse string minus but not include the final space as thats how we did this here.
the solution below basically does the same thing only using string slicing to reverse the string
"""
def reverseWords(s):

        

        s =s.split(" ")

        strings = ""
        for i in s:

            for j in range(len(i)-1,-1,-1):
                strings+=i[j]
            
            strings+= " "
            
        
        return strings[:-1] #return everything except the last space

def reverseWords2(s):
        res = s.split(" ")
        for i in range(len(res)):
            res[i] = res[i][::-1]
        return " ".join(res)

