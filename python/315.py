"""
315. Count of Smaller Numbers After Self

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""

"""
1. Binary Indexed Tree O(n*log max(nums)): use binary indexed tree to find the number of numbers less than i
"""

class Solution(object):
  def countSmaller(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if not nums:
      return []
    min_number = min(nums)
    nums = [num - min_number + 1 for num in nums]
    max_number = max(nums)
    tree = BinaryIndexedTree(max_number)
    result = []
    for num in reversed(nums):
      result.append(tree.sum(num - 1))
      tree.add(num, 1)
    return result[::-1]

class BinaryIndexedTree(object):
  def __init__(self, max_number):
    self.array = [0] * (max_number + 1)
    self.max_number = max_number

  def lowbit(self, x):
    return x & -x

  def add(self, index, number):
    while index <= self.max_number:
      self.array[index] += 1
      index += self.lowbit(index)

  def sum(self, index):
    s = 0
    while index > 0:
      s += self.array[index]
      index -= self.lowbit(index)
    return s

s = Solution()
assert (s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0])
assert (s.countSmaller([1, 2, 3, 4]) == [0, 0, 0, 0])
assert (s.countSmaller([4, 3, 2, 1]) == [3, 2, 1, 0])
