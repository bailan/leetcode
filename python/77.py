"""
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
  def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def dfs(n, k, start_number, path, result):
      if len(path) == k:
        result.append(path)
        return
      for number in range(start_number, n):
        dfs(n, k, number + 1, path + [number + 1], result)

    result = []
    dfs(n, k, 0, [], result)
    return result

