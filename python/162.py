"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] != num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -\infinity.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""

import sys

class Solution(object):
  def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [-sys.maxint] + nums + [-sys.maxint]
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) / 2
      if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
        return mid - 1
      elif nums[mid] > nums[mid - 1]:
        left = mid
      else:
        right = mid

s = Solution()
assert (s.findPeakElement([1, 2, 3, 1]) == 2)
assert (s.findPeakElement([1, 2]) == 1)
assert (s.findPeakElement([2, 1]) == 0)