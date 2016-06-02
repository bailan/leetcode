"""
140. Word Break II

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

"""
DFS + Trie: LTE
DP + Trie: LTE
DP + hashtable: LTE
DP + Memo 
"""

class Solution(object):
  """
  :type s: str
  :type wordDict: Set[str]
  :rtype: bool
  """

  def wordBreak(self, s, wordDict):
    memo = {}
    return self.wordBreakMemo(s, wordDict, memo)

  def wordBreakMemo(self, s, wordDict, memo):
    if not s:
      return ['']
    if s in memo:
      return memo[s]
    result = []
    for word in wordDict:
      length = len(word)
      if s[:length] == word:
        for w in self.wordBreakMemo(s[length:], wordDict, memo):
          if w:
            result.append(word + ' ' + w)
          else:
            result.append(word)
    memo[s] = result
    return result
  
  def wordBreakHash(self, s, wordDict):
    dictionary = {}
    longest_word_length = 0
    for word in wordDict:
      dictionary[word] = True
      longest_word_length = max(longest_word_length, len(word))
    n = len(s)
    f = [[] for _ in range(n)]
    for i in range(n):
      start_j = max(0, i - longest_word_length + 1)
      word = ''
      for j in reversed(range(start_j, i + 1)):
        word = s[j] + word
        if word in dictionary:
          if j == 0:
            f[i].append([word])
          else:
            f[i].extend([words + [word] for words in f[j - 1]])
    return [' '.join(words) for words in f[-1]]

  def wordBreakTrie(self, s, wordDict):
    trieroot = TrieNode()
    for word in wordDict:
      trieroot.insert(word[::-1])
    n = len(s)
    f = [[] for _ in range(n)]
    for i in range(n):
      node = trieroot
      for j in reversed(range(i + 1)):
        if s[j] in node.children:
          node = node.children[s[j]]
          if node.word:
            if j == 0:
              f[i].append([node.word[::-1]])
            else:
              f[i].extend([words + [node.word[::-1]] for words in f[j - 1]])
    return [' '.join(words) for words in f[-1]]

class TrieNode(object):
  def __init__(self):
    self.word = None
    self.children = {}

  def insert(self, word):
    node = self
    for letter in word:
      if letter not in node.children:
        node.children[letter] = TrieNode()
      node = node.children[letter]
    node.word = word

s = Solution()
print s.wordBreak("leetcode", ["leet", "code"])
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])