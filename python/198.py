"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

"""
DP O(n) f[i] = max(f[i - 2] + v[i], f[i - 1])
"""

class Solution(object):
  def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current = previous = previous_previous = 0
    for num in nums:
      current = max(previous, previous_previous + num)
      previous_previous = previous
      previous = current
    return current