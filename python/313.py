#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
313. Super Ugly Number

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""

"""
1. O(nk) number[index[i]] * primes[i]
2. Heap O(nlogk)
"""

import heapq

class Solution(object):
  def nthSuperUglyNumber(self, n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """ 
    k = len(primes)
    numbers = [1]
    index = [0] * k
    for i in range(1, n):
      candidates = [primes[j] * numbers[index[j]] for j in range(k)]
      numbers.append(min(candidates))
      for j in range(k):
        if candidates[j] == numbers[-1]:
          index[j] += 1
    return numbers[-1]

  def nthSuperUglyNumberUsingHeap(self, n, primes):
    numbers = [1]
    heap = []
    for prime in primes:
      heapq.heappush(heap, (prime, prime, 0))
    for i in range(1, n):
      number, prime, index = heapq.heappop(heap)
      numbers.append(number)
      heapq.heappush(heap, (prime * numbers[index + 1], prime, index + 1))
      while number == heap[0][0]:
        num, prm, idx = heapq.heappop(heap)
        heapq.heappush(heap, (prm * numbers[idx + 1], prm, idx + 1))
    return numbers[-1]

s = Solution()
assert (s.nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32)
assert (s.nthSuperUglyNumber(1, [2]) == 1)
assert (s.nthSuperUglyNumber(4, [2]) == 8)
assert (s.nthSuperUglyNumber(5, [2, 3]) == 6)