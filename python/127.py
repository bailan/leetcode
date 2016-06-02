"""
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
  def ladderLength(self, beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: Set[str]
    :rtype: int
    """
    def one_diff(word):
      n = len(word)
      for i in range(n):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          if c != word[i]:
            yield word[:i] + c + word[i + 1:]

    begin_words = set([beginWord])
    end_words = set([endWord])
    explore_words = set(wordList)
    distance = 2
    while end_words:
      new_explored_words = set()
      for word in begin_words:
        for new_word in one_diff(word):
          if new_word in explore_words:
            explore_words.remove(new_word)
            new_explored_words.add(new_word)
          if new_word in end_words:
            return distance
      print explore_words
      distance += 1
      begin_words, end_words = end_words, new_explored_words
    return 0
    

s = Solution()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])