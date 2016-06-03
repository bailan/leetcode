"""
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""

class Solution(object):
  def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    number_a = list(a)
    number_b = list(b)
    number_a = [0] * (len(b) - len(a)) + number_a
    number_b = [0] * (len(a) - len(b)) + number_b
    carry = 0
    for i in reversed(range(len(number_a))):
      carry = int(number_a[i]) + int(number_b[i]) + carry
      number_a[i] = str(carry % 2)
      carry = carry / 2
    if carry:
      number_a = ['1'] + number_a
    return ''.join(number_a)

s = Solution()
print s.addBinary("11", "1")
print s.addBinary("0", "1")
print s.addBinary("1111", "1")