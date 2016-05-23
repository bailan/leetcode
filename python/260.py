"""
260. Single Number III

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""

"""
get a xor b, then use the lowbit(a xor b) to split the array into one with a and another with b
"""
class Solution(object):
  def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    a_xor_b = 0
    for num in nums:
      a_xor_b ^= num
    lowbit = a_xor_b & -a_xor_b
    a, b = 0, 0
    for num in nums:
      if num & lowbit:
        a ^= num
      else:
        b ^= num
    return [a, b]

s = Solution()
assert (set(s.singleNumber([1, 2, 1, 3, 2, 5])) == set([3, 5]))
assert (set(s.singleNumber([1, 2])) == set([1, 2]))
assert (set(s.singleNumber([1, 1, 2, 2, 3, 4])) == set([3, 4]))