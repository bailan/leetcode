"""
242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""

import collections

class Solution(object):
  def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    d = collections.defaultdict(int)
    for c in s:
      d[c] += 1
    for c in t:
      if d[c] == 0:
        return False
      d[c] -= 1
    return True

s = Solution()
assert (s.isAnagram("anagram", "nagaram"))
assert (s.isAnagram("rat", "car") == False)
