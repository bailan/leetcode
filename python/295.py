"""
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
"""

"""
1. array: add O(n), query O(1)
2. two heaps: add O(logn), query O(1)
"""

import heapq

class MedianFinder:
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.min_heap = []
    self.max_heap = []

  def addNum(self, num):
    """
    Adds a num into the data structure.
    :type num: int
    :rtype: void
    """
    if len(self.min_heap) == len(self.max_heap):
      if not self.min_heap or num < self.min_heap[0]:
        heapq.heappush(self.max_heap, -num)
      else:
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    else:
      if num >= -self.max_heap[0]:
        heapq.heappush(self.min_heap, num)
      else:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

  def findMedian(self):
    """
    Returns the median of current data stream
    :rtype: float
    """
    if len(self.min_heap) == len(self.max_heap):
      return float(self.min_heap[0] - self.max_heap[0]) / 2
    else:
      return -self.max_heap[0]
        

# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(2)
assert (mf.findMedian() == 2)
mf.addNum(3)
assert (mf.findMedian() == 2.5)
mf.addNum(4)
assert (mf.findMedian() == 3)
