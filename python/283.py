"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

"""
1. Idea of Partition: O(n)
2. move non-zero to fron: O(n)
"""

class Solution(object):
  def moveZeroes(self, nums):
    n = len(nums)
    non_zero_index = 0
    for i in range(n):
      if nums[i]:
        nums[non_zero_index] = nums[i]
        non_zero_index += 1
    for i in range(non_zero_index, n):
      nums[i] = 0
    return nums

  def moveZeroesByPartition(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    zero_index = 0
    for i in range(n):
      if nums[i]:
        nums[zero_index], nums[i] = nums[i], nums[zero_index]
        zero_index += 1
    return nums

s = Solution()
assert (s.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0])
assert (s.moveZeroes([0]) == [0])
assert (s.moveZeroes([1]) == [1])
assert (s.moveZeroes([1, 0]) == [1, 0])
assert (s.moveZeroes([0, 1]) == [1, 0])


