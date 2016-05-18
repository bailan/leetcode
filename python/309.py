"""
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
"""

"""
1. DP O(n^2)
f[i] = max{p[i] - p[j] + g[j - 2]} p[i] > p[j] and i > j
g[i] = max{f[j]} j < i
2. Greedy O(n) remove the profit after cool down from the cost
"""

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    cost = max(prices)
    max_profit = 0
    max_profit_with_cool_down = 0
    for price in prices:
      cost = min(price - max_profit_with_cool_down, cost)
      max_profit_with_cool_down = max_profit
      max_profit = max(price - cost, max_profit)
    return max_profit

s = Solution()
assert (s.maxProfit([1, 2, 3, 0, 2]) == 3)