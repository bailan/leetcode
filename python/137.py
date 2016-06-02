"""
137. Single Number II

Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

"""
count the occurence of 1 in each bit
"""

class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    one = 0
    two = 0
    for num in nums:
      one, two = (num ^ one) & ~two, ~(num ^ one) & (one | two)
    return one ^ two

s = Solution()
assert (s.singleNumber([1,1,1,2]) == 2)
assert (s.singleNumber([1,1,1,2,2]) == 2)