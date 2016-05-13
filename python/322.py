"""
322. Coin Change

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
  coins = [1, 2, 5], amount = 11
  return 3 (11 = 5 + 5 + 1)

Example 2:
  coins = [2], amount = 3
  return -1.
"""

"""
DP, O(nm)
"""

import sys

class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    f = [0]
    for i in range(amount):
      number = sys.maxint
      for coin in coins:
        if i + 1 - coin >= 0 and number > f[i + 1 - coin] + 1:
          number = f[i + 1 - coin] + 1
      f.append(number)
    if f[-1] == sys.maxint:
      return -1
    else:
      return f[-1]

s = Solution()
assert (s.coinChange([1,2,5], 11) == 3)
assert (s.coinChange([2], 3) == -1)
assert (s.coinChange([1,6,10], 12) == 2)
