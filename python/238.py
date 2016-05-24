"""
238. Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""
Consider the 0!
first pass: product[i] = product before i
second pass: product[i] = product[i] * product after i
"""

class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    result = [1]
    for i in range(n - 1):
      result.append(result[-1] * nums[i])
    product = 1
    for i in reversed(range(n)):
      result[i] *= product
      product *= nums[i]
    return result

s = Solution()
assert (s.productExceptSelf([1,2,3,4]) == [24,12,8,6])
assert (s.productExceptSelf([1,0,1]) == [0,1,0])
