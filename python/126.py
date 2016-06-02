"""
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution(object):
  def findLadders(self, beginWord, endWord, wordlist):
    """
    :type beginWord: str
    :type endWord: str
    :type wordlist: Set[str]
    :rtype: List[List[int]]
    """
    def one_diff(word):
      n = len(word)
      for i in range(n):
        for c in 'abcdefghijklmnopqrstuvwxyz':
          if c != word[i]:
            yield word[:i] + c + word[i + 1:]

    def path(word1, word2, backtrack, begin_word):
      path1 = []
      gen_path(word1, [word1], path1, backtrack)
      path2 = []
      gen_path(word2, [word2], path2, backtrack)
      if path2[0][-1] == begin_word:
        path1, path2 = path2, path1
      return [p1[::-1] + p2 for p1 in path1 for p2 in path2]

    def gen_path(word, path, paths, backtrack):
      if not backtrack[word]:
        paths.append(path)
        return
      for w in backtrack[word]:
        gen_path(w, path + [w], paths, backtrack)

    begin_words = set([beginWord])
    end_words = set([endWord])
    explore_words = set(wordlist) - begin_words - end_words
    backtrack = {beginWord : None, endWord : None}
    result = []
    while end_words:
      new_words = set()
      for word in begin_words:
        for new_word in one_diff(word):
          if new_word in end_words:
            result.extend(path(word, new_word, backtrack, beginWord))
          if new_word in explore_words:
            new_words.add(new_word)
            if new_word in backtrack:
              backtrack[new_word].append(word)
            else:
              backtrack[new_word] = [word]
      explore_words = explore_words - new_words
      if result:
        break
      begin_words, end_words = end_words, new_words
    return result

s = Solution()
print s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
print s.findLadders("hit", "cog", ["hot","cog","dot","dog","hit","lot","log"])