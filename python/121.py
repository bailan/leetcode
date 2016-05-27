"""
121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

"""

import sys

class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    min_price = sys.maxint
    for price in prices
      min_price = min(price, min_price)
      profit = max(price - min_price, profit)
    return profit