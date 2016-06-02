"""
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

"""
DP
f[i] = min(f[i-1], f[i]) + a[i]
"""


class Solution(object):
  def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    f = [0] * n
    for i in range(n):
      if i:
        f[i] = f[i - 1] + triangle[i][i]
      else:
        f[i] = triangle[i][i]
      for j in reversed(range(i)):
        if j:
          f[j] = min(f[j], f[j - 1]) + triangle[i][j]
        else:
          f[j] = f[j] + triangle[i][j]
    return min(f)