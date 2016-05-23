
"""
274. H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researchers h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.
"""

"""
1. Sort O(nlogn)
2. Citation number table O(n)
"""

class Solution(object):
  def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    citation_number = [0 for _ in range(n + 1)]
    for c in citations:
      citation_number[min(c, n)] += 1
    number_of_citation_larger_than_i = 0
    for i in reversed(range(n + 1)):
      number_of_citation_larger_than_i += citation_number[i]
      if number_of_citation_larger_than_i >= i:
        return i
    return 0

s = Solution()
assert (s.hIndex([3, 0, 6, 1, 5]) == 3)
assert (s.hIndex([1]) == 1)
assert (s.hIndex([0]) == 0)
assert (s.hIndex([]) == 0)