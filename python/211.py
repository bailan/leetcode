"""
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

"""
Trie add O(l) search O(\sigma l)
"""

class WordDictionary(object):
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.is_word = False
    self.children = {}    

  def addWord(self, word):
    """
    Adds a word into the data structure.
    :type word: str
    :rtype: void
    """
    node = self
    for letter in word:
      if letter not in node.children:
        node.children[letter] = WordDictionary()
      node = node.children[letter]
    node.is_word = True

  def search(self, word):
    """
    Returns if the word is in the data structure. A word could
    contain the dot character '.' to represent any one letter.
    :type word: str
    :rtype: bool
    """
    if not word:
      return self.is_word
    if word[0] == '.':
      for letter in self.children.keys():
        if self.children[letter].search(word[1:]):
          return True
      return False
    else:
      if word[0] not in self.children:
        return False
      return self.children[word[0]].search(word[1:])

# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
assert (wordDictionary.search("pad") == False)
assert (wordDictionary.search("bad"))
assert (wordDictionary.search(".ad"))
assert (wordDictionary.search("b.."))