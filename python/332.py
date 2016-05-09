"""
332. Reconstruct Itinerary

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""

"""
greedy dfs
1. O(m + m*n) adjacent list
2. O(m*logn) adjacent heap
"""

import heapq

class Solution(object):
  def findItinerary(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    flights = {}
    for ticket in tickets:
      if ticket[0] not in flights:
        flights[ticket[0]] = []
      heapq.heappush(flights[ticket[0]], ticket[1])
    current = 'JFK'
    itinerary = []
    stack = [current]
    while stack:
      if current in flights and flights[current]:
        stack.append(current)
        current = heapq.heappop(flights[current])
      else:
        itinerary.append(current)
        current = stack.pop() 
    return itinerary[::-1]

s = Solution()
assert (s.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == ["JFK", "MUC", "LHR", "SFO", "SJC"])
assert (s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"])
assert (s.findItinerary([["JFK", "AAA"], ["JFK", "BBB"], ["AAA", "JFK"], ["BBB", "JFK"]]) == ["JFK", "AAA", "JFK", "BBB", "JFK"])
assert (s.findItinerary([["JFK", "AAA"], ["JFK", "BBB"], ["AAA", "JFK"], ["BBB", "JFK"], ["AAA", "BBB"], ["BBB", "AAA"]]) == ["JFK", "AAA", "BBB", "AAA", "JFK", "BBB", "JFK"])
assert (s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ["JFK", "NRT", "JFK", "KUL"])
