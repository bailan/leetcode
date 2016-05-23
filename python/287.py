"""
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

"""
cycle dection O(n), start from a[n], the index needs to be decremented by one
"""

class Solution(object):
  def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow = nums[-1] - 1
    fast = nums[nums[-1] - 1] - 1
    while fast != slow:
      fast = nums[nums[fast] - 1] - 1
      slow = nums[slow] - 1
    slow = -1
    while fast != slow:
      fast = nums[fast] - 1
      slow = nums[slow] - 1
    return slow + 1

s = Solution()
assert (s.findDuplicate([2, 4, 1, 2, 3]) == 2)
assert (s.findDuplicate([1, 1]) == 1)
assert (s.findDuplicate([1, 1, 2, 3, 4]) == 1)
assert (s.findDuplicate([4, 1, 2, 3, 4]) == 4)
