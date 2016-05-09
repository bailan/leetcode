#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
335. Self Crossing

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)
"""

"""
the ith line crosses any previous lines if and only if the ith line crosses the (i-3)th, (i-4)th or (i-5)th line.
"""

class Solution(object):
  def isSelfCrossing(self, x):
    """
    :type x: List[int]
    :rtype: bool
    """
    n = len(x)
    for i in range(3, n):
      if x[i] >= x[i-2] and x[i-3] >= x[i-1]:
        return True
      elif i > 3 and x[i-1] == x[i-3] and x[i] >= x[i-2] - x[i-4]:
        return True
      elif i > 4 and x[i-2] >= x[i-4] and x[i] >= x[i-2] - x[i-4] and x[i-3] >= x[i-1] and x[i-1] >= x[i-3] - x[i-5]:
        return True
    return False

s = Solution()
assert (s.isSelfCrossing([2,1,1,2]))
assert (s.isSelfCrossing([1,2,3,4]) == False)
assert (s.isSelfCrossing([1,1,1,1]))
assert (s.isSelfCrossing([1,2,2,2,1]))
assert (s.isSelfCrossing([1,2,3,2,1]) == False)
assert (s.isSelfCrossing([1,2,2,3,2]) == False)
assert (s.isSelfCrossing([1,1,2,2,1,1]))
assert (s.isSelfCrossing([1,1,2,2,2,1]))
assert (s.isSelfCrossing([1,1,2,2,3,2]) == False)
assert (s.isSelfCrossing([1,3,2,2,1,1]) == False)
assert (s.isSelfCrossing([1,1,2,2,3,3,4,4,10,4,4,3,3,2,2,1,1]) == False)
