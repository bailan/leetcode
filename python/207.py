"""
207. Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
"""

"""
Topological sort O(m + n) dfs or bfs
"""

import collections

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    in_degree = [0] * numCourses
    out_node = [[] for _ in range(numCourses)]
    for edge in prerequisites:
      in_degree[edge[1]] += 1
      out_node[edge[0]].append(edge[1])
    queue = collections.deque()
    topo = []
    for i in range(numCourses):
      if in_degree[i] == 0:
        queue.appendleft(i)
    while queue:
      i = queue.pop()
      topo.append(i)
      for j in out_node[i]:
        in_degree[j] -= 1
        if in_degree[j] == 0:
          queue.appendleft(j)
      out_node[i] = []
    return len(topo) == numCourses

s = Solution()
assert (s.canFinish(2, [[1,0]]))
assert (s.canFinish(2, [[1,0], [0,1]]) == False)
assert (s.canFinish(2, []))