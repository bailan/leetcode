"""
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""

"""
DP: O(n^2)
    if m[i][j] == 1:
      f[i][j] = min(f[i-1][j-1] + 1, row, column[j])
      row += 1
      column[j] += 1
    else:
      f[i][j] = 0
      row = 0
      column[j] = 0
"""

class Solution(object):
  def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
      return 0
    m = len(matrix)
    n = len(matrix[0])
    column = [0 for _ in range(n)]
    f = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
      f[0][i] = column[i] = int(matrix[0][i])
    for i in range(1, m):
      row = 0
      for j in range(n):
        if j == 0 or matrix[i][j] == "0":
          f[i][j] = column[j] = row = int(matrix[i][j])
        else:
          row += 1
          column[j] += 1
          f[i][j] = min(f[i - 1][j - 1] + 1, row, column[j])
    area = 0
    for i in range(m):
      for j in range(n):
        area = max(area, f[i][j]**2)
    return area

s = Solution()
assert (s.maximalSquare(["10100", "10111", "11111", "10010"]) == 4)
assert (s.maximalSquare(["11", "11"]) == 4)
assert (s.maximalSquare(["0001","1101","1111","0111","0111"]) == 9)