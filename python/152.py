"""
152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

"""
DP O(n)
if a[i] >= 0:
  max_product[i] = max(max_product[i - 1], 1) * a[i]
  min_product[i] = min(min_product[i - 1], 1) * a[i] 
if a[i] < 0:
  max_product[i] = min(min_product[i - 1], 1) * a[i]
  min_product[i] = max(max_product[i - 1], 1) * a[i] 
"""

class Solution(object):
  def maxProduct(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    max_product = min_product = product = nums[0]
    for i in range(1, n):
      if nums[i] >= 0:
        max_product, min_product = max(max_product, 1) * nums[i], min(min_product, 1) * nums[i]
      else:
        max_product, min_product = min(min_product, 1) * nums[i], max(max_product, 1) * nums[i]
      product = max(max_product, product)
    return product

s = Solution()
assert (s.maxProduct([2,3,-2,4]) == 6)
assert (s.maxProduct([-1,-2,-3,-4]) == 24)
assert (s.maxProduct([-1,1,-1,1]) == 1)
assert (s.maxProduct([-1]) == -1)
