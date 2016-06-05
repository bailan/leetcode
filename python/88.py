"""
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution(object):
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    for i in reversed(range(m)):
      nums1[n + i] = nums1[i]
    i = 0
    j = 0
    while j < n and i < m:
      if nums1[i + n] < nums2[j]:
        nums1[i + j] = nums1[i + n]
        i += 1
      else:
        nums1[i + j] = nums2[j]
        j += 1
    while j < n:
      nums1[i + j] = nums2[j]
      j += 1
    return nums1

s = Solution()
assert (s.merge([1,0,0], 1, [2,3], 2) == [1, 2, 3])
assert (s.merge([1], 1, [], 0))
