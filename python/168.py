"""
168. Excel Sheet Column Title My Submissions QuestionEditorial Solution
Total Accepted: 61993 Total Submissions: 281871 Difficulty: Easy
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""

class Solution(object):
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    title = ''
    while n:
      title = chr(ord('A') + (n - 1) % 26) + title
      n = (n - 1) / 26
    return title