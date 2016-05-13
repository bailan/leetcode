#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
327. Count of Range Sum

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.
"""

"""
O(n^2) find s[j] - s[i] in [lower, upper]
O(nlogn) by divide and conquer based on merge sort
"""

class Solution(object):
  def countRangeSum(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    n = len(nums)
    s = [0]
    for i in range(n):
      s.append(s[i] + nums[i])
    return self.count_range_sum(s, 0, n, lower, upper)

  def count_range_sum(self, s, left, right, lower, upper):
    if left == right:
      return 0
    mid = (left + right) / 2
    count = self.count_range_sum(s, left, mid, lower, upper)
    count += self.count_range_sum(s, mid + 1, right, lower, upper)
    count += self.count_range_sum_cross_mid(s, left, right, mid, lower, upper)
    self.merge(s, left, right, mid)
    return count
  
  def count_range_sum_cross_mid(self, s, left, right, mid, lower, upper):
    count = 0
    i = left
    j = mid + 1
    k = mid + 1
    while i <= mid:
      while j <= right and s[j] - s[i] < lower:
        j += 1
      while k <= right and s[k] - s[i] <= upper:
        k += 1
      i += 1
      count += k - j
    return count

  def merge(self, s, left, right, mid):
    t = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
      if s[i] < s[j]:
        t.append(s[i])
        i += 1
      else:
        t.append(s[j])
        j += 1
    while i <= mid:
      t.append(s[i])
      i += 1
    while j <= right:
      t.append(s[j])
      j += 1
    for i in range(right - left + 1):
      s[left + i] = t[i]

s = Solution()
assert (s.countRangeSum([-2, 5, -1], -2, 2) == 3)
assert (s.countRangeSum([1,2,3], 1, 6) == 6)
assert (s.countRangeSum([1,2,3], 1, 2) == 2)
assert (s.countRangeSum([1], 1, 1) == 1)
assert (s.countRangeSum([0, 0], -1, 1) == 3)
assert (s.countRangeSum([2147483647,-2147483648,-1,0], -1, 0) == 4)
assert (s.countRangeSum([-3,1,2,-2,2,-1], -3, -1) == 7)
