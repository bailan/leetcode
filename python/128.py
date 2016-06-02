"""
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    hashtable = {}
    for num in nums:
      hashtable[num] = True
    longest = 0
    for num in nums:
      low = num
      while low - 1 in hashtable:
        low -= 1
        del hashtable[low]
      high = num
      while high + 1 in hashtable:
        high += 1
        del hashtable[high]
      longest = max(longest, high - low + 1)
    return longest