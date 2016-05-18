"""
310. Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
"""

"""
Topological sort: find degree 1 nodes, remove them, repeat, return the last batch
"""

class Solution(object):
  def findMinHeightTrees(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    adjacent_set = [set() for _ in range(n)]
    for edge in edges:
      adjacent_set[edge[0]].add(edge[1])
      adjacent_set[edge[1]].add(edge[0])
    nodes_to_remove = [i for i in range(n) if len(adjacent_set[i]) <= 1]
    while nodes_to_remove:
      new_nodes_to_remove = []
      for from_node in nodes_to_remove:
        if adjacent_set[from_node]:
          to_node = adjacent_set[from_node].pop()
          adjacent_set[to_node].remove(from_node)
          if len(adjacent_set[to_node]) == 1:
            new_nodes_to_remove.append(to_node)
      if not new_nodes_to_remove:
        break
      nodes_to_remove = new_nodes_to_remove
    return nodes_to_remove

s = Solution()
assert (s.findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]) == [1])
assert (s.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]) == [3, 4])
assert (s.findMinHeightTrees(1, []) == [0])