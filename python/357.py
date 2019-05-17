"""
357. Count Numbers with Unique Digits
Medium

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10^n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(k):
            if k == 0:
                return 1
            t = 9
            for i in range(9, 9 - k + 1, -1):
                t *= i
            return t
        return sum([f(i) for i in range(n + 1)])