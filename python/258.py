"""
258. Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime? 
"""

"""
10->1, 11->2, 12->3, 13->4, 14->5, 15->6, 16->7, 17->8, 18->9
19->1, 20->2 ...
"""

class Solution(object):
  def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if not num:
      return 0
    else:
      return (num - 1) % 9 + 1