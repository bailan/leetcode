"""
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

class Solution(object):
  def findWords(self, board, words):
    """
    :type board: List[List[str]]
    :type words: List[str]
    :rtype: List[str]
    """
    root = TrieNode()
    for word in words:
      root.insert(word)
    m, n = len(board), len(board[0])
    result = []
    visited = [[False for _ in range(n)] for _ in range(m)]
    for x in range(m):
      for y in range(n): 
        self.dfs(board, x, y, m, n, root, visited, result)
    return list(result)

  def dfs(self, board, x, y, m, n, node, visited, result):
    if visited[x][y]:
      return
    if board[x][y] not in node.children:
      return
    node = node.children[board[x][y]]
    if node.word:
      result.append(node.word)
      node.word = None
    visited[x][y] = True
    if x + 1 < m:
      self.dfs(board, x + 1, y, m, n, node, visited, result)
    if x - 1 >= 0:
      self.dfs(board, x - 1, y, m, n, node, visited, result)
    if y + 1 < n:
      self.dfs(board, x, y + 1, m, n, node, visited, result)
    if y - 1 >= 0:
      self.dfs(board, x, y - 1, m, n, node, visited, result)
    visited[x][y] = False

class TrieNode(object):
  def __init__(self):
    self.word = None
    self.children = {}

  def insert(self, word):
    node = self
    for letter in word:
      if letter not in node.children:
        node.children[letter] = TrieNode()
      node = node.children[letter]
    node.word = word

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
s = Solution()
assert (set(s.findWords(board, words)) == set(["eat","oath"]))
assert (set(s.findWords(board, ["a", "aa", "aaa"])) == set(["a","aa", "aaa"]))
