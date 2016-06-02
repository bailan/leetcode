"""
134. Gas Station

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
"""

"""
gas(0) >= cost(0)
gas(0) + gas(1) >= cost(0) + gas(1)
gas(0) + ... + gas(k) >= cost(0) + ... + cost(k)
"""

class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    n = len(gas)
    gas = gas + gas
    cost = cost + cost
    accumulative_gas = 0
    accumulative_cost = 0
    start_index = 0
    for i in range(2*n - 1):
      accumulative_gas += gas[i]
      accumulative_cost += cost[i]
      if accumulative_gas < accumulative_cost:
        accumulative_gas = 0
        accumulative_cost = 0
        start_index = i + 1
      elif i - start_index == n - 1:
        return start_index
    return -1


