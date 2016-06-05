"""
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

class Solution(object):
  def maximalRectangle(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix:
      return 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    for i in range(m):
      for j in range(n):
        heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

      small_index_on_left = [0] * n
      stack = [0]
      for j in range(1, n):
        while stack and heights[stack[-1]] >= heights[j]:
          stack.pop()
        small_index_on_left[j] = stack[-1] + 1 if stack else 0
        stack.append(j)

      small_index_on_right = [n] * n
      stack = [n - 1]
      for j in reversed(range(n - 1)):
        while stack and heights[stack[-1]] >= heights[j]:
          stack.pop()
        small_index_on_right[j] = stack[-1] if stack else n
        stack.append(j)

      for j in range(n):
        max_area = max(max_area, heights[j] * (small_index_on_right[j] - small_index_on_left[j]))

    return max_area

s = Solution()
print s.maximalRectangle(["1101","1101","1111"])