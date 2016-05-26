"""
214. Shortest Palindrome

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""

"""
the KMP next table:
aacecaaa#aaacecaa
01000120012234567
"""

class Solution(object):
  def shortestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    m = self.get_next(s + "#" + s[::-1])[-1]
    return s[:m-1:-1] + s

  def get_next(self, s):
    n = len(s)
    next = [0] * n
    i, j = 1, 0
    while i < n:
      while j and s[i] != s[j]:
        j = next[j - 1]
      if s[i] == s[j]:
        j += 1
      next[i] = j
      i += 1 
    return next

s = Solution()
assert (s.shortestPalindrome("aacecaaa") == "aaacecaaa")
assert (s.shortestPalindrome("abcd") == "dcbabcd")
assert (s.shortestPalindrome("ababbbabbaba") == "ababbabbbababbbabbaba")