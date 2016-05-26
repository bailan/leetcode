"""
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class TrieNode(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.is_word = False
    self.children = {}
    

class Trie(object):

  def __init__(self):
    self.root = TrieNode()

  def insert(self, word):
    """
    Inserts a word into the trie.
    :type word: str
    :rtype: void
    """
    node = self.root
    for letter in word:
      if letter not in node.children:
        node.children[letter] = TrieNode()
      node = node.children[letter]
    node.is_word = True

  def search(self, word):
    """
    Returns if the word is in the trie.
    :type word: str
    :rtype: bool
    """
    node = self.root
    for letter in word:
      if letter not in node.children:
        return False
      node = node.children[letter]
    return node.is_word

  def startsWith(self, prefix):
    """
    Returns if there is any word in the trie
    that starts with the given prefix.
    :type prefix: str
    :rtype: bool
    """
    node = self.root
    for letter in prefix:
      if letter not in node.children:
        return False
      node = node.children[letter]
    return True

# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("ann")
trie.insert("ana")
trie.insert("anna")
trie.insert("anne")
assert (trie.search("ann"))
assert (trie.search("ana"))
assert (trie.search("anna"))
assert (trie.search("anne"))
assert (trie.search("") == False)
assert (trie.search("an") == False)
assert (trie.search("ane") == False)
assert (trie.search("annie") == False)
assert (trie.startsWith(""))
assert (trie.startsWith("a"))
assert (trie.startsWith("an"))
assert (trie.startsWith("ann"))
assert (trie.startsWith("b") == False)