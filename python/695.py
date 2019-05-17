"""
695. Max Area of Island
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    queue = deque()
                    queue.append((i, j))
                    total = 0
                    while queue:
                        (x, y) = queue.popleft()
                        visited[x][y] = True
                        total += 1
                        if x + 1 < n and grid[x + 1][y] and not visited[x + 1][y]:
                            queue.append((x + 1, y))
                        if x - 1 >= 0 and grid[x - 1][y] and not visited[x - 1][y]:
                            queue.append((x - 1, y))
                        if y + 1 < m and grid[x][y + 1] and not visited[x][y + 1]:
                            queue.append((x, y + 1))
                        if y - 1 >= 0 and grid[x][y - 1] and not visited[x][y - 1]:
                            queue.append((x, y - 1))
                    max_area = max(max_area, total)
        return max_area

matrix = [[0,0,0,0,0,0,0,0]]
print Solution().maxAreaOfIsland(matrix)
                        
        

        