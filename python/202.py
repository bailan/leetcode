"""
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

"""
1->1, 2->4->16->37->58->89->145->42->20->4, 3->9->81->65->61->37, 4, 5->25->29->85->89, 6->36->45->41->17->50, 7->49->97->130->10->1
8->64->52->29, 9, 10->1, 11->2, 12->5, 13->10->1, 14->17->5
1,7 happy
"""

class Solution(object):
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    square = [x*x for x in range(10)]
    while True:
      s = 0
      while n:
        s += square[n % 10]
        n = n / 10
      if s < 10:
        if s == 1 and s == 7:
          return True
        else:
          return False
      n = s