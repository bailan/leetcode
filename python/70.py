"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution(object):
  def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
      return 1
    elif n == 2:
      return 2
    prev = 1
    current = 2
    for i in range(2, n):
      current, prev = current + prev, current
    return current