"""
189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
"""

"""
1. Reverse 1~n, reverse 1~k, reverse (k+1)~n
"""

class Solution(object):
  def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    for i in range(n/2):
      nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
    for i in range(k/2):
      nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
    for i in range((n-k)/2):
      nums[k + i], nums[n - i - 1] = nums[n - i - 1], nums[k + i]
    return nums

s = Solution()
assert (s.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
assert (s.rotate([1,2,3,4,5,6,7], 7) == [1,2,3,4,5,6,7])
assert (s.rotate([1,2,3,4,5,6,7], 0) == [1,2,3,4,5,6,7])
assert (s.rotate([1,2,3,4,5,6,7], 8) == [7,1,2,3,4,5,6])