"""
233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

Beware of overflow.
"""

"""
Count 1 in each digit
"""

class Solution(object):
  def countDigitOne(self, n):
    """
    :type n: int
    :rtype: int
    """
    total_ones = 0
    base = 1
    low, high = 0, n
    while high > 0:
      current = high % 10 
      high = high / 10
      total_ones += high * base
      if current > 1:
        total_ones += base
      elif current == 1:
        total_ones += low + 1
      low = low + current * base
      base = base * 10
    return total_ones

s = Solution()
assert (s.countDigitOne(13) == 6)
assert (s.countDigitOne(1) == 1)
assert (s.countDigitOne(0) == 0)