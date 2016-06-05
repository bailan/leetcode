"""
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
  def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
      return 0
    n = len(nums)
    length = 0
    count = 0
    prev = nums[0] - 1
    for i in range(n):
      if nums[i] == prev and count < 2:
        nums[length] = nums[i]
        length += 1
        count += 1
      elif nums[i] != prev:
        nums[length] = nums[i]
        length += 1
        count = 1
        prev = nums[i]
    return length
    