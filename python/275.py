"""
275. H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm? 
"""

"""
Binary search O(logn)
"""

class Solution(object):
  def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    left = 0
    right = n - 1
    while left < right:
      mid = (left + right) / 2
      if citations[mid] >= n - mid:
        right = mid
      else:
        left = mid + 1
    if n == 0 or citations[left] < n - left:
      return 0
    else:
      return n - left

s = Solution()
assert (s.hIndex([0, 1, 3, 5, 6]) == 3)
assert (s.hIndex([1]) == 1)
assert (s.hIndex([0]) == 0)
assert (s.hIndex([0, 0]) == 0)
assert (s.hIndex([]) == 0)