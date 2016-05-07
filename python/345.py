"""
345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".
"""

"""
INPUT: contains uppercase
O(n): swap 1st with last, swap 2rd with 2rd to the last, ...
"""


class Solution(object):
  def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowels = 'aeiouAEIOU'
    words = list(s)
    left = 0
    right = len(words) - 1
    while left < right:
      while left < right and words[left] not in vowels:
        left += 1
      while left < right and words[right] not in vowels:
        right -= 1
      words[left], words[right] = words[right], words[left]
      left += 1
      right -= 1
    return ''.join(words)

s = Solution()
assert (s.reverseVowels('hello') == 'holle')
assert (s.reverseVowels('leetcode') == 'leotcede')
assert (s.reverseVowels('a') == 'a')
assert (s.reverseVowels('b') == 'b')
assert (s.reverseVowels('ab') == 'ab')
assert (s.reverseVowels('ba') == 'ba')
assert (s.reverseVowels('aeiou') == 'uoiea')
assert (s.reverseVowels('aA') == 'Aa') # uppercase
