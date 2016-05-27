"""
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

"""
DP O(n)
profit_before[i] = max(profit_before[i - 1], prices[i] - min_before[i])
profit_after[i] = max(profit_after[i + 1], max_after[i] - prices[i])
"""

import sys

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    n = len(prices)
    profit_before = [0] * n
    min_price = sys.maxint
    for i in range(1, n):
      min_price = min(min_price, prices[i - 1])
      profit_before[i] = max(profit_before[i - 1], prices[i] - min_price)
    profit_after = [0] * n
    max_price = 0
    for i in reversed(range(n - 1)):
      max_price = max(max_price, prices[i + 1])
      profit_after[i] = max(profit_after[i + 1], max_price - prices[i])
    profit = profit_after[0]
    for i in range(1, n - 1):
      profit = max(profit_before[i] + profit_after[i + 1], profit)
    return profit

s = Solution()
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])