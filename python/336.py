"""
336. Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""

"""
CORNER CASE
O(nl^2)
"""

class Solution(object):
  def palindromePairs(self, words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    n = len(words)
    reversed_words = {}
    for i in range(n):
      reversed_words[words[i][::-1]] = i
    result = []
    for i in range(n):
      for j in range(len(words[i])+1):
        prefix = words[i][:j]
        suffix = words[i][j:]
        if prefix in reversed_words and reversed_words[prefix] != i and self.is_palindrome(suffix):
          result.append([i, reversed_words[prefix]])
        if j and suffix in reversed_words and reversed_words[suffix] != i and self.is_palindrome(prefix):
          result.append([reversed_words[suffix], i])
    return result

  def is_palindrome(self, s):
    l = len(s)
    for i in range(l / 2):
      if s[i] != s[l - i - 1]:
        return False
    return True

s = Solution()
assert (s.palindromePairs(["bat", "tab", "cat"]) == [[0, 1], [1, 0]])
assert (s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]) == [[0, 1], [1, 0], [3, 2], [2, 4]])
assert (s.palindromePairs(["a", "aa", "aaa"]) == [[1, 0], [0, 1], [2, 0], [1, 2], [2, 1], [0, 2]])
assert (s.palindromePairs(["a", ""]) == [[0, 1], [1, 0]])
