"""
318. Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""

"""
Bitmap O(n^2)
"""

class Solution(object):
  def maxProduct(self, words):
    """
    :type words: List[str]
    :rtype: int
    """
    words.sort(key = len, reverse=True)
    n = len(words)
    masks = [0] * n
    for i in range(n):
      for c in words[i]:
        masks[i] |= 1 << (ord(c) - ord('a'))
    max_product = 0
    for i in range(n):
      if len(words[i]) * len(words[i]) > max_product:
        for j in range(i + 1, n):
          if masks[i] & masks[j] == 0:
            max_product = max(len(words[i]) * len(words[j]), max_product)
    return max_product

s = Solution()
assert (s.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16)
assert (s.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4)
assert (s.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0)