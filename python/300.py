"""
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

"""
DP O(n^2)
DP + Binary Search O(nlogn)
"""

class Solution(object):
  def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    smallest_number_of_length = [0]
    for num in nums:
      left = 0
      right = len(smallest_number_of_length) - 1
      while left < right:
        mid = (left + right + 1) / 2
        if smallest_number_of_length[mid] < num:
          left = mid 
        else:
          right = mid - 1
      if left + 1 == len(smallest_number_of_length):
        smallest_number_of_length.append(num)
      else:
        smallest_number_of_length[left + 1] = num
    return len(smallest_number_of_length) - 1

s = Solution()
assert (s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4)