"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution(object):
  def trailingZeroes(self, n):
    """
    :type n: int
    :rtype: int
    """
    zero = 0
    while n:
      n = n / 5
      zero += n
    return zero