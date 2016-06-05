"""
81. Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""

class Solution(object):
  def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    left, right = 0, len(nums) - 1
    while left < right:
      mid = (left + right) / 2
      if nums[mid] == target:
        return True
      if nums[left] < nums[mid]:
        if nums[left] <= target <= nums[mid]:
          right = mid
        else:
          left = mid + 1
      elif nums[left] > nums[mid]:
        if nums[mid] <= target <= nums[right]:
          left = mid
        else:
          right = mid - 1
      else:
        left += 1
    return nums[left] == target
    