"""
78. Subsets

Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
  def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def dfs(array, index, path, result):
      if index == len(array):
        result.append(path)
        return
      dfs(array, index + 1, path, result)
      dfs(array, index + 1, path + [array[index]], result)

    result = []
    dfs(sorted(nums), 0, [], result)
    return result

s = Solution()
print s.subsets([1,2,3])