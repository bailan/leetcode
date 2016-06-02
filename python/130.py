"""
130. Surrounded Regions

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

import collections

class Solution(object):
  def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    if not board:
      return board
    m, n = len(board), len(board[0])
    queue = collections.deque()
    for y in range(n):
      if board[0][y] == 'O':
        board[0][y] = 'A'
        queue.appendleft((0, y))
      if board[m - 1][y] == 'O':
        board[m - 1][y] = 'A'
        queue.appendleft((m - 1, y))
    for x in range(m):
      if board[x][0] == 'O':
        board[x][0] = 'A'
        queue.appendleft((x, 0))
      if board[x][n - 1] == 'O':
        board[x][n - 1] = 'A'
        queue.appendleft((x, n - 1))
    while queue:
      (x, y) = queue.pop()
      if x + 1 < m and board[x + 1][y] == 'O':
        board[x + 1][y] = 'A'
        queue.appendleft((x + 1, y)) 
      if x - 1 >= 0 and board[x - 1][y] == 'O':
        board[x - 1][y] = 'A'
        queue.appendleft((x - 1, y)) 
      if y + 1 < n and board[x][y + 1] == 'O':
        board[x][y + 1] = 'A'
        queue.appendleft((x, y + 1)) 
      if y - 1 >= 0 and board[x][y - 1] == 'O':
        board[x][y - 1] = 'A'
        queue.appendleft((x, y - 1))
    for x in range(m):
      for y in range(n):
        if board[x][y] == 'O':
          board[x][y] = 'X'
        elif board[x][y] == 'A':
          board[x][y] = 'O'
    return board

board = [
  ['X', 'X', 'X', 'X'],
  ['X', 'O', 'O', 'X'],
  ['X', 'X', 'O', 'X'],
  ['X', 'O', 'X', 'X']
]
s = Solution()
print s.solve(board)