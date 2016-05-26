"""
204. Count Primes

Description:

Count the number of prime numbers less than a non-negative number, n.
"""

"""
Sieve
"""

class Solution(object):
  def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
      return 0
    primes = [1] * n
    primes[0] = primes[1] = 0
    prime = 2
    while prime * prime < n:
      i = prime * prime
      while i < n:
        primes[i] = 0
        i += prime
      prime += 1
      while primes[prime] == 0:
        prime += 1
    return sum(primes)