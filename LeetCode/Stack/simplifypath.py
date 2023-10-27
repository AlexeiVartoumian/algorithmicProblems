"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
 
Constraints:
1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""

"""
this problem deal with various "unix style" stings and asks us to return it in canonical form as in the way its supposed to be. for example consider the following strings /home/2, //home//fooo, //..// , //b./c we have to simplify the folowing. as such there are three main cases to consider
1. if the directory name "." occurs then we can ignore it as it means stay in the current directory.
2. if the directotry name  ".." occurs then we can pop it from the stack as it means to go back up one directory
3.the third case would be neither occurs , which means we have encountered a path to a current directory and we add it to our stack.

eg : path = "/home/" => /home
eg : path = "/../" =>   /
eg : path = "/home//foo" => /home/foo

notice how all the output paths start with a back slash. as such the approach is to first split the string by "/" meaning we disregard all of them. then handle first case where we ignore both "." and "" to account for the split array space.
second case will be to handle the ".." if there is a stack then pop off last element as e want to go back one up the file tree
third case: add it to the stack. finally return "/" as thats the base case and add base case to the joined array with a "/" separating the each item if the stack exists
"""

def simplifypath(path):

    stack = []

    for currentdirectory in path.split("/"):
        
        if currentdirectory == "." or currentdirectory== "":
            continue
        elif currentdirectory == "..":
            if stack:
                stack.pop()
        else:
            stack.append(currentdirectory)

    return "/" + "/".join(stack)