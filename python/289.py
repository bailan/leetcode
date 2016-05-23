"""
289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

"""
In-place: bit manipulation
"""

class Solution(object):
  def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    m = len(board)
    n = len(board[0])
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    for row in range(m):
      for column in range(n):
        lives = 0
        for i in range(len(dx)):
          x = row + dx[i]
          y = column + dy[i]
          if 0 <= x < m and 0 <= y < n:
            lives += board[x][y] & 1    
        if (board[row][column] & 1 == 0 and lives == 3) or (board[row][column] & 1 == 1 and 2 <= lives <= 3):
          board[row][column] |= 2
    for row in range(m):
      for column in range(n):
        board[row][column] >>= 1