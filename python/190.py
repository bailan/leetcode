"""
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution(object):
  def reverseBits(self, n):
    """
    :type n: int
    :rtype: int
    """
    reverse = 0
    for i in range(32):
      reverse = (reverse << 1) | (n & 1)
      n >>= 1
    return reverse