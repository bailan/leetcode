"""
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""

class Solution(object):

  TWENTY = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', \
    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
  TENS = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

  def numberToWords(self, num):
    """
    :type num: int
    :rtype: str
    """
    if not num:
      return 'Zero'
    return self.number_to_words(num).strip()

  def number_to_words(self, num):
    if not num:
      return ''
    elif num < 20:
      return ' ' + Solution.TWENTY[num]
    elif num < 100:
      return ' ' + Solution.TENS[num / 10] + self.number_to_words(num % 10)
    elif num < 1000:
      return self.number_to_words(num / 100) + ' Hundred' + self.number_to_words(num % 100)
    elif num < 1000000:
      return self.number_to_words(num / 1000) + ' Thousand' + self.number_to_words(num % 1000)
    elif num < 1000000000:
      return self.number_to_words(num / 1000000) + ' Million' + self.number_to_words(num % 1000000)
    else:
      return self.number_to_words(num / 1000000000) + ' Billion' + self.number_to_words(num % 1000000000)
    
s = Solution()
assert (s.numberToWords(123) == "One Hundred Twenty Three")
assert (s.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five")
assert (s.numberToWords(1234567) == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
assert (s.numberToWords(0) == 'Zero')
assert (s.numberToWords(1) == 'One')
assert (s.numberToWords(10) == 'Ten')
assert (s.numberToWords(11) == 'Eleven')
assert (s.numberToWords(20) == 'Twenty')
assert (s.numberToWords(21) == 'Twenty One')
assert (s.numberToWords(99) == 'Ninety Nine')
assert (s.numberToWords(100) == 'One Hundred')
assert (s.numberToWords(101) == 'One Hundred One')
assert (s.numberToWords(110) == 'One Hundred Ten')
assert (s.numberToWords(199) == 'One Hundred Ninety Nine')