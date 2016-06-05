"""
33. Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""

class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) / 2
      if nums[left] < nums[mid]:
        if nums[left] <= target <= nums[mid]:
          right = mid
        else:
          left = mid + 1
      else:
        if nums[mid] <= target <= nums[right]:
          left = mid
        else:
          right = mid - 1
    return left if nums[left] == target else -1
