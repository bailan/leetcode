"""
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""

import sys

class Solution(object):
  def maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 2:
      return 0
    max_number = max(nums)
    min_number = min(nums)
    bucket_size = (max_number - min_number) / n + 1
    bucket_min = [sys.maxint] * n
    bucket_max = [-sys.maxint] * n

    for num in nums:
      bucket_number = (num - min_number) / bucket_size
      bucket_min[bucket_number] = min(bucket_min[bucket_number], num)
      bucket_max[bucket_number] = max(bucket_max[bucket_number], num)
    
    gap = 0
    last = 0
    for i in range(1, n):
      if bucket_min[i] != sys.maxint:
        gap = max(gap, bucket_min[i] - bucket_max[last])
        last = i
    return gap

s = Solution()
#assert (s.maximumGap([1,2,4,5]) == 2)
#assert (s.maximumGap([1]) == 0)
#assert (s.maximumGap([1,1,1,1]) == 0)
assert (s.maximumGap([3,6,9,1]) == 3)