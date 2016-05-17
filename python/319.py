"""
319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

  Given n = 3. 

  At first, the three bulbs are [off, off, off].
  After first round, the three bulbs are [on, on, on].
  After second round, the three bulbs are [on, off, on].
  After third round, the three bulbs are [on, off, off]. 

  So you should return 1, because there is only one bulb is on.
"""

"""
Math O(n): perfect squares have a pair of identical divisor
"""

class Solution(object):
  def bulbSwitch(self, n):
    """
    :type n: int
    :rtype: int
    """
    i = 0
    while i*i <= n:
      i += 1
    return i - 1

s = Solution()
assert (s.bulbSwitch(3) == 1)
assert (s.bulbSwitch(1) == 1)
assert (s.bulbSwitch(4) == 2)
assert (s.bulbSwitch(9) == 3)
