"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
  def wordPattern(self, pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    mapping = {}
    mapped = {}
    n = len(pattern)
    words = str.split()
    if n != len(words):
      return False
    for i in range(n):
      if pattern[i] not in mapping:
        if words[i] not in mapped:
          mapping[pattern[i]] = words[i]
          mapped[words[i]] = True
        else:
          return False
      elif mapping[pattern[i]] != words[i]:
        return False
    return True

s = Solution()
assert (s.wordPattern("abba", "dog cat cat dog"))
assert (s.wordPattern("abba", "dog cat cat fish") == False)
assert (s.wordPattern("aaaa", "dog cat cat dog") == False)
assert (s.wordPattern("abba", "dog dog dog dog") == False)
assert (s.wordPattern("", "dog") == False)
assert (s.wordPattern("a", "") == False)
assert (s.wordPattern("", "") == True)

