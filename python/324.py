"""
324. Wiggle Sort II

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
import random

class Solution(object):
  def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    random.shuffle(nums)
    median = self.find_median(nums)
    nums[::2], nums[1::2] = nums[(n-1)/2::-1], nums[:(n-1)/2:-1]
    return nums

  def find_median(self, nums):
    n = len(nums)
    return self.find_kth_element(nums, 0, n-1, n/2 + 1)

  def find_kth_element(self, array, left, right, k):
    pivot = array[right]
    second_start = left
    second_end = right - 1
    current = left
    while current <= second_end:
      if array[current] < pivot:
        array[second_start], array[current] = array[current], array[second_start]
        second_start += 1
        current += 1
      elif array[current] > pivot:
        array[second_end], array[current] = array[current], array[second_end]
        second_end -= 1
      else:
        current += 1
    second_end += 1
    array[second_end], array[right] = array[right], array[second_end]
    if second_start - left >= k:
      return self.find_kth_element(array, left, second_start - 1, k)
    elif second_end - left + 1 < k:
      return self.find_kth_element(array, second_end + 1, right, k - (second_end - left + 1) )
    else:
      return array[second_start]

s = Solution()
# test for find_median
assert (s.find_median([2,3,1,4,5]) == 3)
assert (s.find_median([1,1,1,1,1]) == 1)
assert (s.find_median([1,2,3,4]) == 3)
assert (s.find_median([1]) == 1)

def wiggle(array):
  if len(array) < 2:
    return True
  if array[0] >= array[1]:
    return False
  diff = [array[i+1] - array[i] for i in range(len(array) - 1)]
  for i in range(len(diff) - 1):
    if diff[i] * diff[i + 1] >= 0:
      return False
  return True

assert (wiggle(s.wiggleSort([1, 5, 1, 1, 6, 4])))
assert (wiggle(s.wiggleSort([1, 3, 2, 2, 3, 1])))
assert (wiggle(s.wiggleSort([1,2,3,4,5])))
assert (wiggle(s.wiggleSort([1,1,1,2,2])))
