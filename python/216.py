"""
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""

"""
DFS
"""

class Solution(object):
  def combinationSum3(self, k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    result = []
    self.dfs(1, k, n, [], result)
    return result

  def dfs(self, smallest, k, n, path, result):
    if k == 1:
      if smallest <= n < 10:
        result.append(path + [n])
      return
    for i in range(smallest, 10):
      self.dfs(i + 1, k - 1, n - i, path + [i], result)

s = Solution()
assert (s.combinationSum3(3, 7) == [[1,2,4]])
assert (s.combinationSum3(3, 9) == [[1,2,6], [1,3,5], [2,3,4]])
assert (s.combinationSum3(1, 2) == [[2]])
