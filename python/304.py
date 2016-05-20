#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

"""
DP O(n^2) s[i][j] = s[i-1][j] + sum_j a[i][j]
"""

class NumMatrix(object):
  def __init__(self, matrix):
    """
    initialize your data structure here.
    :type matrix: List[List[int]]
    """
    self.matrix = matrix
    self.n = len(matrix)
    if self.n:
      self.m = len(matrix[0])
    else:
      self.m = 0
    self.s = [[0 for _ in range(self.m + 1)] for _ in range(self.n + 1)]
    for row in range(self.n):
      sum_of_current_row = 0
      for column in range(self.m):
        sum_of_current_row += self.matrix[row][column]
        self.s[row + 1][column + 1] = self.s[row][column + 1] + sum_of_current_row  

  def sumRegion(self, row1, col1, row2, col2):
    """
    sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
    :type row1: int
    :type col1: int
    :type row2: int
    :type col2: int
    :rtype: int
    """
    if row1 < 0 or row2 < 0 or row1 >= self.n or row2 >= self.n:
      return 0
    if col1 < 0 or col2 < 0 or col1 >= self.m or col2 >= self.m:
      return 0
    if row1 > row2 or col1 > col2:
      return 0
    return self.s[row2 + 1][col2 + 1] + self.s[row1][col1] \
      - self.s[row1][col2 + 1] - self.s[row2 + 1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
assert (numMatrix.sumRegion(2, 1, 4, 3) == 8)
assert (numMatrix.sumRegion(1, 1, 2, 2) == 11)
assert (numMatrix.sumRegion(1, 2, 2, 4) == 12)