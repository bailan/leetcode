"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than |_n/3_| times. The algorithm should run in linear time and in O(1) space.
"""

"""
Keep two candidates
"""


class Solution(object):
  def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    candidate1 = candidate2 = 0
    count1 = count2 = 0
    for num in nums:
      if candidate1 == num:
        count1 += 1
      elif candidate2 == num:
        count2 += 1
      elif count1 == 0:
        candidate1 = num
        count1 = 1
      elif count2 == 0:
        candidate2 = num
        count2 = 1
      else:
        count1 -= 1
        count2 -= 1
    n = len(nums)
    result = []
    count1 = count2 = 0
    for num in nums:
      if candidate1 == num:
        count1 += 1
      elif candidate2 == num:
        count2 += 1
    if count1 > n/3:
      result.append(candidate1)
    if count2 > n/3:
      result.append(candidate2)
    return result

s = Solution()
assert (s.majorityElement([1,2,3]) == [])
assert (s.majorityElement([1,1,3]) == [1])
assert (s.majorityElement([1,1,2,2,3]) == [1,2])
