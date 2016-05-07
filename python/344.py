"""
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""

class Solution(object):
  def reverseString(self, s):
    """
    :type s: str
    :rtype: str
    """
    l = list(s)
    left = 0
    right = len(l) - 1
    while left < right:
      l[left], l[right] = l[right], l[left]
      left += 1
      right -= 1
    return ''.join(l)

s = Solution()
assert (s.reverseString('hello') == 'olleh')
assert (s.reverseString('a') == 'a')
assert (s.reverseString('ab') == 'ba')
assert (s.reverseString('aa') == 'aa')
assert (s.reverseString('abc') == 'cba')
assert (s.reverseString('') == '')
assert (s.reverseString('a@b#c') == 'c#b@a')
assert (s.reverseString('a   ') == '   a')
