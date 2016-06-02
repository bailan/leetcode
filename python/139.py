"""
139. Word Break

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

"""
DFS + Trie: LTE
DP + Hashtable f[i] = f[j] if s[j:i+1] is a word in dictionary
"""

class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: bool
    """
    dictionary = {}
    longest_word_length = 0
    for word in wordDict:
      dictionary[word] = True
      longest_word_length = max(longest_word_length, len(word))
    n = len(s)
    f = [False] * n
    for i in range(n):
      word = ''
      j_start = max(0, i - longest_word_length + 1)
      for j in reversed(range(j_start, i + 1)):
        word = s[j] + word
        if word in dictionary and (j == 0 or f[j - 1]):
          f[i] = True
          break
    return f[-1]

s = Solution()
print s.wordBreak("leetcode", ["leet", "code"])