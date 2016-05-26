"""
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""

class Solution(object):
  def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
      return False
    n = len(s)
    s_map = {}
    t_map = {}
    for i in range(n):
      if s[i] not in s_map:
        s_map[s[i]] = t[i]
      elif s_map[s[i]] != t[i]:
        return False
      if t[i] not in t_map:
        t_map[t[i]] = s[i]
      elif t_map[t[i]] != s[i]:
        return False
    return True