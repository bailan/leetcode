"""
171. Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
"""

class Solution(object):
  def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    number = 0
    for c in s:
      number = number * 26 + ord(c) - ord('A') + 1
    return number