"""
368. Largest Divisible Subset
Medium

443

22

Favorite

Share
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums = sorted(nums)
        n = len(nums)
        size = [1 for _ in range(n)]
        index = [-1 for _ in range(n)]
        max_index = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and size[i] < size[j] + 1:
                    size[i] = size[j] + 1
                    index[i] = j
            if size[i] > size[max_index]:
                max_index = i
        
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = index[max_index]
        return result