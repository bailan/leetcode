"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

"""
DP O(n^2)
f[i][j] = f[i-1][j] and s1[i-1] == s3[i+j-1] or f[i][j-1] and s2[j-1] == s3[i+j-1]
"""

class Solution(object):
  def isInterleave(self, s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    n = len(s1)
    m = len(s2)
    if len(s3) != n + m:
      return False
    f = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    f[0][0] = True
    for i in range(1, m + 1):
      f[0][i] = f[0][i - 1] and s2[i - 1] == s3[i - 1]
    for i in range(1, n + 1):
      f[i][0] = f[i - 1][0] and s1[i - 1] == s3[i - 1]
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        f[i][j] = f[i-1][j] and s1[i-1] == s3[i+j-1] or f[i][j-1] and s2[j-1] == s3[i+j-1]     
    return f[n][m]

s = Solution()
assert (s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
assert (s.isInterleave("aabcc", "dbbca", "aadbbbaccc") == False)