"""
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

"""
DP
"""

class Solution(object):
  def minCut(self, s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    palindrome = [[False for _ in range(n)] for _ in range(n)] 
    f = [n] * n
    for right_index in range(n):
      for left_index in range(right_index + 1):
        if s[left_index] == s[right_index] and (left_index + 1 > right_index - 1 or palindrome[left_index + 1][right_index - 1]):
          palindrome[left_index][right_index] = True
          if left_index == 0:
            f[right_index] = 0
          else:
            f[right_index] = min(f[right_index], f[left_index - 1] + 1)
    return f[-1]

s = Solution()
assert (s.minCut("aab") == 1)
assert (s.minCut("abbab") == 1)