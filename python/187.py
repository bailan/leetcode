"""
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
  def findRepeatedDnaSequences(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    letter_to_number = {'A':0, 'C':1, 'G':2, 'T':3}
    occur = {}
    n = len(s)
    sequence = 0
    result = []
    for i in range(n):
      sequence = ((sequence << 2) & 0xfffff) + letter_to_number[s[i]]
      if i > 8:
        if sequence not in occur:
          occur[sequence] = 0
        occur[sequence] += 1
        if occur[sequence] == 2:
          result.append(s[i-9:i+1])
    return result

s = Solution()
assert (s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC", "CCCCCAAAAA"])