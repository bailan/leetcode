"""
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""

"""
small_index_on_left = [0, 0, 2, 3, 1, 5]
small_index_on_right = [1, 6, 4, 4, 6, 6]
area = max(heights[i] * (small_index_on_right[i] - small_index_on_left[i]))
"""

class Solution(object):
  def largestRectangleArea(self, heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    n = len(heights)
    small_index_on_left = [0] * n
    stack = [0]
    for i in range(1, n):
      while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
      if stack:
        small_index_on_left[i] = stack[-1] + 1
      else:
        small_index_on_left[i] = 0
      stack.append(i)

    small_index_on_right = [n] * n
    stack = [n - 1]
    for i in reversed(range(n - 1)):
      while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
      if stack:
        small_index_on_right[i] = stack[-1]
      else:
        small_index_on_right[i] = n
      stack.append(i)

    max_area = 0
    for i in range(n):
      max_area = max(max_area, heights[i] * (small_index_on_right[i] - small_index_on_left[i]))
    return max_area


s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])