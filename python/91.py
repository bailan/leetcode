"""
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
  def numDecodings(self, s):
    """
    :type s: str
    :rtype: int
    """
    def valid(s):
      return 1 <= int(s) <= 26 and s == str(int(s))

    if not s:
      return 0
    n = len(s)
    f = [0] * (n + 1)
    f[0] = 1
    f[1] = 1 if valid(s[0]) else 0
    for i in range(1, n):
      if valid(s[i]):
        f[i + 1] += f[i]
      if valid(s[i - 1:i + 1]):
        f[i + 1] += f[i - 1]
    return f[-1]

s = Solution()
print s.numDecodings("12")
print s.numDecodings("111")
print s.numDecodings("101")
