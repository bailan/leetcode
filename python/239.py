#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""

"""
Deque
"""

import collections

class Solution(object):
  def maxSlidingWindow(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    n = len(nums)
    max_queue = collections.deque()
    result = []
    for i in range(n):
      while max_queue and nums[max_queue[-1]] < nums[i]:
        max_queue.pop()
      max_queue.append(i)
      if i >= k - 1:
        result.append(nums[max_queue[0]])
        if max_queue[0] == i - k + 1:
          max_queue.popleft()
    return result

s = Solution()
assert (s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7])
assert (s.maxSlidingWindow([1], 1) == [1])