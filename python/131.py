"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""

"""
DP
f[i] = f[j] + s[j+1, i+1] if s[j+1][i+1] is palindrome
"""

class Solution(object):
  def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    n = len(s)
    palindrome = [[False for _ in range(n)] for _ in range(n)]
    f = [[] for _ in range(n)]
    for i in range(n):
      for j in range(i + 1):
        if s[j] == s[i] and (j + 1 > i - 1 or palindrome[j + 1][i - 1]):
          palindrome[j][i] = True
          if j == 0:
            f[i].append([s[:i + 1]])
          elif f[j - 1]:
            for partition in f[j - 1]:
              f[i].append(partition + [s[j:i + 1]])
    return f[-1]

s = Solution()
assert (sorted(s.partition("aab")) == sorted([["aa","b"], ["a","a","b"]]))