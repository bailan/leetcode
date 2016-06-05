"""
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution(object):
  def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    def dfs(board, word, m, n, x, y, i, visited):
      if visited[x][y]:
        return False
      if word[i] != board[x][y]:
        return False
      if i == len(word) - 1:
        return True
      visited[x][y] = True
      if x + 1 < m and dfs(board, word, m, n, x + 1, y, i + 1, visited) or \
        x - 1 >= 0 and dfs(board, word, m, n, x - 1, y, i + 1, visited) or \
        y + 1 < n and dfs(board, word, m, n, x, y + 1, i + 1, visited) or \
        y - 1 >= 0 and dfs(board, word, m, n, x, y - 1, i + 1, visited):
        return True
      visited[x][y] = False
      return False

    if not board:
      return False
    m, n = len(board), len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    for x in range(m):
      for y in range(n):
        if dfs(board, word, m, n, x, y, 0, visited):
          return True
    return False