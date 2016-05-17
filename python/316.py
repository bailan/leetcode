"""
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""

"""
O(n) find each letter one by one
"""

class Solution(object):
  def removeDuplicateLetters(self, s):
    """
    :type s: str
    :rtype: str
    """
    occur = [0 for _ in range(26)]
    for c in s:
      occur[ord(c) - ord('a')] += 1
    result = []
    chosen = [False for _ in range(26)]
    for c in s:
      occur[ord(c) - ord('a')] -= 1
      if chosen[ord(c) - ord('a')]:
        continue
      while result and result[-1] > c and occur[ord(result[-1]) - ord('a')]: 
        chosen[ord(result.pop()) - ord('a')] = False
      result.append(c)
      chosen[ord(c) - ord('a')] = True
    return ''.join(result)

  def removeDuplicateLettersUsingMask(self, s):
    """
    :type s: str
    :rtype: str
    """
    n = len(s)
    mask = 0
    masks = [0 for _ in range(n)]
    occur = [[] for _ in range(26)]
    for i in reversed(range(n)):
      ordinal = ord(s[i]) - ord('a')
      mask = mask | 1 << ordinal
      masks[i] = mask
      occur[ordinal].append(i)
    right = 0
    while right < n and masks[right] == mask:
      right += 1
    current_mask = 0
    result = []
    while current_mask != mask:
      for letter in range(26):
        if occur[letter] and occur[letter][-1] < right:
          position = occur[letter][-1]
          occur[letter] = []
          for l in range(26):
            while occur[l] and occur[l][-1] <= position:
              occur[l].pop()
          current_mask |= 1 << letter
          while right < n and masks[right] | current_mask == mask:
            right += 1
          result.append(chr(letter + ord('a')))
          break
    return ''.join(result)

s = Solution()
assert (s.removeDuplicateLetters("bcabc") == "abc")
assert (s.removeDuplicateLetters("cbacdcbc") == "acdb")
assert (s.removeDuplicateLetters("baab") == "ab")
assert (s.removeDuplicateLetters("abacb") == "abc")
