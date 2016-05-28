"""
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""

"""
DP
f[i][j]: the max profit that until the jth day with at most i transactions
f[i][j] = max(f[i][j - 1], f[i - 1][x] + prices[j] - prices[x]) x<j
        = max(f[i][j - 1], max(f[i - 1][x] - prices[x] + prices[j]) 
g[i][j] = max(f[i][x] - prices[x] + prices[j])
        = max(g[i][j - 1], f[i][j - 1]) - prices[j - 1] + prices[j])
"""

class Solution(object):
  def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
      return 0
    n = len(prices)
    f = [0] * n
    g = [0] * n
    if k >= n/2:
      return self.avoid_timeout(prices)
    for i in range(k):
      for j in range(1, n):
        g[j] = max(g[j - 1], f[j - 1]) + prices[j] - prices[j - 1]
      for j in range(1, n):
        f[j] = max(f[j - 1], g[j])
      print f, g
    return max(f)

  def avoid_timeout(self, prices):
    profit = 0
    n = len(prices)
    for i in range(1, n):
      profit += max(0, prices[i] - prices[i - 1])
    return profit

s = Solution()
assert (s.maxProfit(1, [1, 2, 1, 2, 1, 2]) == 1)
assert (s.maxProfit(2, [1, 2, 1, 2, 1, 2]) == 2)
assert (s.maxProfit(3, [1, 2, 1, 2, 1, 2]) == 3)
assert (s.maxProfit(2, [6,1,3,2,4,7]) == 7)