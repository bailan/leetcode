"""
115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""

"""
DP
f[i][j] = f[i][j-1] + f[i-1][j-1]  if t[i] = s[j]
          f[i][j-1]  if t[i] != s[j]
"""
class Solution(object):
  def numDistinct(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    m, n = len(t), len(s)
    f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(n + 1):
      f[0][i] = 1
    for i in range(1, m + 1):
      for j in range(1, n + 1):
        f[i][j] = f[i][j - 1]
        if t[i - 1] == s[j - 1]:
          f[i][j] += f[i - 1][j - 1]
    return f[m][n]

s = Solution()
print s.numDistinct("rabbbit", "rabbit")