"""
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

"""
DP O(n^{1.5}): f(i) = min(f(i-j*j)) + 1, i >= j*j
"""

import math

class Solution(object):
  
  f = [0]

  def numSquares(self, n):
    """
    :type n: int
    :rtype: int
    """
    squares = [i*i for i in range(1, int(math.sqrt(n)) + 1)]  
    for i in range(len(self.f), n + 1):
      number_of_squares = i
      for square in squares:
        if i >= square:
          number_of_squares = min(self.f[i - square], number_of_squares)
        else:
          break
      self.f.append(number_of_squares + 1)
    return self.f[n]

s = Solution()
assert (s.numSquares(12) == 3)
assert (s.numSquares(13) == 2)
