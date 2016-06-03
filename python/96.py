"""
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object):
  def numTrees(self, n):
    """
    :type n: int
    :rtype: int
    """
    f = [1, 1]
    for i in range(2, n + 1):
      total = 0
      for j in range(i):
        total += f[j]*f[i-j-1]
      f.append(total)
    return f[-1]