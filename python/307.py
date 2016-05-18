#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
"""

"""
Binary Indexed Tree O(logn)
"""

class NumArray(object):
  def __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.array = nums
    self.tree = BinaryIndexTree(len(nums) + 1)
    for i in range(len(nums)):
      self.tree.add(i + 1, nums[i])

  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: int
    """
    diff = val - self.array[i]
    self.array[i] = val
    self.tree.add(i + 1, diff)    

  def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    return self.tree.sum(j + 1) - self.tree.sum(i)  

class BinaryIndexTree(object):
  def __init__(self, size):
    self.size = size + 1
    self.tree = [0] * self.size

  def lowbit(self, x):
    return x & -x

  def add(self, index, number):
    while index < self.size:
      self.tree[index] += number
      index += self.lowbit(index)

  def sum(self, index):
    s = 0
    while index > 0:
      s += self.tree[index]
      index -= self.lowbit(index)
    return s

# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
assert (numArray.sumRange(0, 2) == 9)
numArray.update(1, 2)
assert (numArray.sumRange(0, 2) == 8)