"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""

"""
BFS
"""

import collections

class Solution(object):
  def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not grid:
      return 0
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    number = 0
    for x in range(m):
      for y in range(n):
        if grid[x][y] == '1' and not visited[x][y]:
          visited[x][y] = True
          self.bfs(grid, m, n, x, y, visited)
          number += 1
    return number
        
  def bfs(self, grid, m, n, x, y, visited):
    queue = collections.deque()
    queue.appendleft((x,y))
    while queue:
      x, y = queue.pop()
      for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1' and not visited[new_x][new_y]:
          queue.appendleft((new_x, new_y))
          visited[new_x][new_y] = True

s = Solution()
assert (s.numIslands(['11110', '11010', '11000', '00000']) == 1)
assert (s.numIslands(['11000', '11000', '00100', '00011']) == 3)