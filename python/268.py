"""
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""
1. Summation
2. XOR
"""

class Solution(object):
  def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    xor = n
    for i in range(n):
      xor ^= i
      xor ^= nums[i]
    return xor

s = Solution()
assert (s.missingNumber([0, 1, 3]) == 2)
assert (s.missingNumber([0]) == 1)