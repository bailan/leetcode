"""
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

Hint:

1. No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
2. Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
3. Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
"""

"""
Be careful about
- Negative numbers
"""

class Solution(object):
  def fractionToDecimal(self, numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    sign = ''
    integer = numerator / denominator
    if integer < 0:
      sign = '-'
    numerator = abs(numerator)
    denominator = abs(denominator)
    integer = (numerator / denominator)
    remainder = numerator % denominator
    if remainder == 0:
      return '{0}{1}'.format(sign, integer)
    divident_index = {}
    fraction = ''
    index = 0
    while remainder:
      divident = remainder * 10
      if divident in divident_index:
        repeat = divident_index[divident]
        return '{0}{1}.{2}({3})'.format(sign, integer, fraction[:repeat], fraction[repeat:])
      else:
        divident_index[divident] = index
      quotient = divident / denominator
      remainder = divident % denominator
      fraction += str(quotient)
      index += 1
    return '{0}{1}.{2}'.format(sign, integer, fraction)

s = Solution()
assert (s.fractionToDecimal(2, 1) == "2")
assert (s.fractionToDecimal(1, 2) == "0.5")
assert (s.fractionToDecimal(2, 3) == "0.(6)")
assert (s.fractionToDecimal(4, 9) == "0.(4)")
assert (s.fractionToDecimal(4, 333) == "0.(012)")
assert (s.fractionToDecimal(0, 1) == "0")
assert (s.fractionToDecimal(1, 4) == "0.25")
assert (s.fractionToDecimal(2, 8) == "0.25")
assert (s.fractionToDecimal(7, 12) == "0.58(3)")
print s.fractionToDecimal(-50, 8)
