"""
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
  def subsetsWithDup(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def dfs(array, index, path, result):
      if index == len(array):
        result.append(path)
        return
      dfs(array, index + 1, path + [array[index]], result)
      while index + 1 < len(array) and array[index + 1] == array[index]:
        index += 1
      dfs(array, index + 1, path, result)

    result = []
    dfs(sorted(nums), 0, [], result)
    return result

s = Solution()
print s.subsetsWithDup([1,2,2])