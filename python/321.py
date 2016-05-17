"""
321. Create Maximum Number

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
  nums1 = [3, 4, 6, 5]
  nums2 = [9, 1, 2, 5, 8, 3]
  k = 5
  return [9, 8, 6, 5, 3]

Example 2:
  nums1 = [6, 7]
  nums2 = [6, 0, 4]
  k = 5
  return [6, 7, 6, 0, 4]

Example 3:
  nums1 = [3, 9]
  nums2 = [8, 9]
  k = 3
  return [9, 8, 9]
"""

"""
1. DP O(n*m*k) f(i, j, k) = max(f(i-1, j, k), f(i, j-1, k), f(i-1, j, k-1) + a[i], f(i, j-1, k-1) + b[j])
2. Merge then DP O((n+m)*k): wrong idea
3. DP + Merge: O((n+m)*k^2) f(i, j) = f(i-1, j), f(i-1, j-1) + a[j]
4. Deque + Merge: O(k(n+m))
"""

import collections

class Solution(object):
  def maxNumber(self, nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """
    result = [0] * k
    for i in range(k + 1):
      if i <= len(nums1) and k - i <= len(nums2):
        result = max(self.merge(self.max_k_subarray(nums1, i), self.max_k_subarray(nums2, k - i)), result)
    return result

  def max_k_subarray(self, array, k):
    result = []
    n = len(array)
    max_queue = collections.deque()
    for i in range(n - k):
      while max_queue and max_queue[-1] < array[i]:
        max_queue.pop()
      max_queue.append(array[i])
    for i in range(n - k, n):
      while max_queue and max_queue[-1] < array[i]:
        max_queue.pop()
      max_queue.append(array[i])
      result.append(max_queue[0])
      max_queue.popleft()
    return result

  def merge(self, array1, array2):
    length1 = len(array1)
    length2 = len(array2)
    index1 = 0
    index2 = 0
    result = []
    while index1 < length1 and index2 < length2:
      if array1[index1] < array2[index2]:
        result.append(array2[index2])
        index2 += 1
      elif array1[index1] > array2[index2]:
        result.append(array1[index1])
        index1 += 1
      else:
        temp_index1 = index1
        temp_index2 = index2
        while temp_index1 < length1 and temp_index2 < length2 and array1[temp_index1] == array2[temp_index2]:
          temp_index1 += 1
          temp_index2 += 1
        if temp_index2 == length2 or temp_index1 < length1 and array1[temp_index1] > array2[temp_index2]:
          result.append(array1[index1])
          index1 += 1
        else:
          result.append(array2[index2])
          index2 += 1
    result.extend(array1[index1:])
    result.extend(array2[index2:])
    return result

s = Solution()
assert (s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3])
assert (s.maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4])
assert (s.maxNumber([3, 9], [8, 9], 3) == [9, 8, 9])
assert (s.maxNumber([1, 2], [], 2) == [1, 2])
