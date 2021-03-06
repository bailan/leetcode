"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""

class Solution(object):
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    majority = 0
    count = 0
    for num in nums:
      if num == majority:
        count += 1
      elif count == 0:
        majority = num
        count += 1
      else:
        count -= 1
    return majority