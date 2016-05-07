"""
347. Top K Frequent Elements 

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

"""
PROBLEM CLARIFICATION: 
- k frequent not numbers appearing k times
- tie?
O(nlogn) sort, count, sort by count
"""

class Solution(object):
  def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    for num in nums:
      if num in count:
        count[num] += 1
      else:
        count[num] = 1
    return sorted(count, key=count.get, reverse=True)[:k]

s = Solution()
assert (s.topKFrequent([1,1,1,2,2,3],2) == [1, 2])
assert (s.topKFrequent([1,1,1,2,2,3],1) == [1])
assert (s.topKFrequent([1,1,1,2,2,3],3) == [1,2,3])
