"""
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""

class Solution(object):
  def summaryRanges(self, nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums:
      return []
    n = len(nums)
    left = right = nums[0]
    result = []
    for i in range(1, n):
      if nums[i] != nums[i - 1] + 1:
        if left == right:
          result.append(str(left))
        else:
          result.append('{0}->{1}'.format(left, right))
        left = right = nums[i]
      else:
        right = nums[i]
    if left == right:
      result.append(str(left))
    else:
      result.append('{0}->{1}'.format(left, right))
    return result

s = Solution()
assert (s.summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"])
assert (s.summaryRanges([0,1]) == ["0->1"])
assert (s.summaryRanges([0,2]) == ["0", "2"])
assert (s.summaryRanges([0]) == ["0"])