"""
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution(object):
  def mySqrt(self, x):
    """
    :type x: int
    :rtype: int
    """
    left = 0
    right = x
    while left < right:
      mid = (left + right + 1) / 2
      square = mid * mid
      if x < square:
        right = mid - 1
      else:
        left = mid
    return left