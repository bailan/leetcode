"""
306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""

"""
Follow the instruction
"""

class Solution(object):
  def isAdditiveNumber(self, num):
    """
    :type num: str
    :rtype: bool
    """
    n = len(num)
    for i in range(1, n/2 + 1): 
      # n-j >= i => j <= n - i
      # n-j >= j-i => j <= (n + i)/2
      for j in range(i + 1, min(n - i, (n + i)/2) + 1):
        number1 = int(num[:i])
        if str(number1) != num[:i]:
          continue
        number2 = int(num[i:j])
        if str(number2) != num[i:j]:
          continue
        if self.isAdditive(num[j:], number1, number2):
          return True
    return False

  def isAdditive(self, string, number1, number2):
    if not string:
      return True
    sum_int = number1 + number2
    sum_string = str(sum_int)
    if string.startswith(sum_string):
      return self.isAdditive(string[len(sum_string):], number2, sum_int)
    return False

s = Solution()
assert (s.isAdditiveNumber("112358"))
assert (s.isAdditiveNumber("199100199"))
assert (s.isAdditiveNumber("111") == False)
assert (s.isAdditiveNumber("101"))