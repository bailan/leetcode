#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""

class NumArray(object):
  def __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.n = len(nums)
    self.s = [0]
    for num in nums:
      self.s.append(self.s[-1] + num)

  def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    if i < 0 or j < 0 or i >= self.n or j >= self.n or i > j:
      return 0
    return self.s[j + 1] - self.s[i]

# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])
assert (numArray.sumRange(0, 2) == 1)
assert (numArray.sumRange(2, 5) == -1)
assert (numArray.sumRange(0, 5) == -3)
assert (numArray.sumRange(0, 0) == -2)