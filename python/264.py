"""
264. Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
  def nthUglyNumber(self, n):
    """
    :type n: int
    :rtype: int
    """
    ugly_numbers = [1]
    index2 = 0
    index3 = 0
    index5 = 0
    for i in range(1, n):
      candidate = min(2 * ugly_numbers[index2], 3 * ugly_numbers[index3], 5 * ugly_numbers[index5])
      if candidate == 2 * ugly_numbers[index2]:
        index2 += 1
      if candidate == 3 * ugly_numbers[index3]:
        index3 += 1
      if candidate == 5 * ugly_numbers[index5]:
        index5 += 1
      ugly_numbers.append(candidate)
    return ugly_numbers[-1]

s = Solution()
assert (s.nthUglyNumber(10) == 12)
assert (s.nthUglyNumber(1) == 1)