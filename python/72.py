"""
72. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

"""
DP O(mn)
f[i][j] = min(f[i - 1][j], f[i - 1][j - 1], f[i][j - 1]) + 1 if word1[i] != word2[j]
          min(f[i - 1][j] + 1, f[i - 1][j - 1], f[i][j - 1] + 1) if word1[i] == word2[j]
"""

class Solution(object):
  def minDistance(self, word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m, n = len(word1), len(word2)
    f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
      f[i][0] = i
    for j in range(1, n + 1):
      f[0][j] = j
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        if word1[i - 1] == word2[j - 1]:
          f[i][j] = min(f[i - 1][j] + 1, f[i - 1][j - 1], f[i][j - 1] + 1)
        else:
          f[i][j] = min(f[i - 1][j], f[i - 1][j - 1], f[i][j - 1]) + 1
    return f[m][n]