"""
220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""

"""
Bucket O(n) key = num/t
"""

class Solution(object):
  def containsNearbyAlmostDuplicate(self, nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    if t < 0:
      return False
    bucket = {}
    n = len(nums)
    for i in range(n):
      key = nums[i] / (t + 1)
      if key in bucket:
        return True
      if key - 1 in bucket and nums[i] - bucket[key - 1] <= t:
        return True
      if key + 1 in bucket and bucket[key + 1] - nums[i] <= t:
        return True
      bucket[key] = nums[i]
      if i >= k:
        del bucket[nums[i - k] / (t + 1)]
    return False

s = Solution()
assert (s.containsNearbyAlmostDuplicate([1, 5, 13, 25, 8, 17], 3, 3))
assert (s.containsNearbyAlmostDuplicate([1, 5, 13, 25, 8, 17], 3, 2) == False)
assert (s.containsNearbyAlmostDuplicate([1, 5, 13, 25, 8, 17], 2, 3) == False)
assert (s.containsNearbyAlmostDuplicate([1, 5, 13, 25, 8, 17], 1, 4))
assert (s.containsNearbyAlmostDuplicate([0], 0, 0) == False)
assert (s.containsNearbyAlmostDuplicate([0, 0], 1, 0))
assert (s.containsNearbyAlmostDuplicate([1, 2], 100, 1))