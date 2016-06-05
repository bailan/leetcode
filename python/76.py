"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution(object):
  def minWindow(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    count = {}
    total = len(t)
    for c in t:
      if c not in count:
        count[c] = 1
      else:
        count[c] += 1
    n = len(s)
    left = right = start = 0
    length = n + 1
    while right < n:
      if s[right] in count:
        count[s[right]] -= 1
        if count[s[right]] >= 0:
          total -= 1
      right += 1
      while not total:
        if s[left] in count:
          count[s[left]] += 1
          if count[s[left]] == 1:
            total += 1
        if right - left < length:
          length = right - left
          start = left
        left += 1
    if length == n + 1:
      return ""
    else:
      return s[start:start + length]

s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")