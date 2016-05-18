#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
312. Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

"""
DP O(n^3) f(i,j) = max(f(i, k) + f(k, j) + a[i][k][j]) i < k < j burst ballon between i and j exclusively.
"""

class Solution(object):
  def maxCoins(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    f = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n):
      for i in range(n - l):
        j = i + l
        for k in range(i + 1, j):
          f[i][j] = max(f[i][k] + f[k][j] + nums[i]*nums[k]*nums[j], f[i][j])
    return f[0][-1]

s = Solution()
print s.maxCoins([3, 1, 5, 8])