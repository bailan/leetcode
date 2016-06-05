"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

"""
Use the first row and column as marker
"""

class Solution(object):
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
      return
    m, n = len(matrix), len(matrix[0])
    first_row_zero = first_column_zero = False
    for x in range(m):
      for y in range(n):
        if matrix[x][y] == 0:
          if x == 0:
            first_row_zero = True
          if y == 0:
            first_column_zero = True
          matrix[x][0] = 0
          matrix[0][y] = 0
    for x in range(1, m):
      for y in range(1, n):
        if matrix[x][0] == 0:
          matrix[x][y] = 0
        elif matrix[0][y] == 0:
          matrix[x][y] = 0
    if first_row_zero:
      for y in range(n):
        matrix[0][y] = 0
    if first_column_zero:
      for x in range(m):
        matrix[x][0] = 0