"""
154. Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.
"""

class Solution(object):
  def findMin(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while True:
      while left < right and nums[left] == nums[right]:
        left += 1
      if nums[left] <= nums[right]:
        return nums[left]
      mid = (left + right) / 2
      if nums[mid] >= nums[left]:
        left = mid + 1
      else:
        right = mid

s = Solution()
assert (s.findMin([4,5,6,7,0,1,2]) == 0)
assert (s.findMin([6,7,0,1,2,4,5]) == 0)
assert (s.findMin([0]) == 0)
assert (s.findMin([0,1]) == 0)
assert (s.findMin([1,0]) == 0)
assert (s.findMin([0,0]) == 0)
assert (s.findMin([1,0,1]) == 0)
assert (s.findMin([1,0,1,1]) == 0)
assert (s.findMin([1,1,0,1]) == 0)