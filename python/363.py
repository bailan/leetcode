"""
363. Max Sum of Rectangle No Larger Than K
Hard

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
Note:

The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""
import sys

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n, m = len(matrix), len(matrix[0])
        prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                prefix_sum[i + 1][j + 1] = matrix[i][j] + prefix_sum[i][j + 1] + prefix_sum[i + 1][j] - prefix_sum[i][j]
        result = -sys.maxint
        for start_x in range(n):
            for start_y in range(m):
                for end_x in range(start_x + 1, n + 1):
                    for end_y in range(start_y + 1, m + 1):
                        s = prefix_sum[end_x][end_y] - prefix_sum[start_x][end_y] - prefix_sum[end_x][start_y] + prefix_sum[start_x][start_y]
                        if s <= k:
                            result = max(result, s)
        return result

print Solution().maxSumSubmatrix([[2,2,-1]], 0)