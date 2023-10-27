"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
"""
"""
use two classes where class one is a tree liek structure with children as an object storing the letter as a key and the treenode class as an object to be used in the other class and a end of word as a boolean. after that its  a case of looping through operations according to the operation specification where we acccess the tree chidlren to see how hey are linked together see below
"""

class Treenode():
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie():

    def __init__(self):
        self.root = Treenode()
    
    def insert(self,string):
        cur = self.root

        for c in string:
            if c not in cur.children:
                cur.children[c] = Treenode()
            cur = cur.children[c]
        cur.endofword = True
    
    def search(self,string):
        cur = self.root

        for c in string:
            if c not in cur.children:
                return False
            cur = c.children[c]
        return cur.endofword
    
    def startswith(self,prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = c.children[c]
        return True


class TreeNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur= cur.children[c]
        cur.endofword = True
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endofword
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True