"""
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.
"""

"""
Partition O(n)
"""

import random

class Solution(object):
  def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    random.shuffle(nums)
    return self.partition(nums, len(nums) - k + 1, 0, len(nums) - 1)

  def partition(self, nums, k, left, right):
    pivot = nums[right]
    first = left
    last = right
    index = left
    while index <= last:
      if nums[index] < pivot:
        nums[index], nums[first] = nums[first], nums[index]
        index += 1
        first += 1
      elif nums[index] == pivot:
        index += 1
      else:
        nums[index], nums[last] = nums[last], nums[index]
        last -= 1
    if first - left >= k:
      return self.partition(nums, k, left, first - 1)
    elif last - left + 1 < k:
      return self.partition(nums, k - last + left - 1, last + 1, right)
    else:
      return nums[first]

s = Solution()
assert (s.findKthLargest([3,2,1,5,6,4], 2) == 5)
assert (s.findKthLargest([3,2,1,5,6,4], 3) == 4)