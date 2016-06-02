"""
133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""

# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

import collections

class Solution(object):
  def cloneGraph(self, node):
    """
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    """
    clone_nodes = {}
    return self.dfs_clone(node, clone_nodes)

  def dfs_clone(self, node, clone_nodes):
    if not node:
      return None
    clone_node = UndirectedGraphNode(node.label)
    clone_nodes[node.label] = clone_node
    for neighbor in node.neighbors:
      if neighbor.label in clone_nodes:
        clone_node.neighbors.append(clone_nodes[neighbor.label])
      else:
        clone_node.neighbors.append(self.dfs_clone(neighbor, clone_nodes))
    return clone_node

  def cloneGraphBFS(self, node):
    """
    :type node: UndirectedGraphNode
    :rtype: UndirectedGraphNode
    """
    if not node:
      return None
    nodes = {}
    start_node = UndirectedGraphNode(node.label)
    nodes[node.label] = start_node
    queue = collections.deque()
    queue.appendleft(node)
    while queue:
      node = queue.pop()
      clone_node = nodes[node.label]      
      for neighbor in node.neighbors:
        if neighbor.label in nodes:
          clone_node.neighbors.append(nodes[neighbor.label])
        else:  
          clone_neighbor = UndirectedGraphNode(neighbor.label)
          nodes[neighbor.label] = clone_neighbor
          clone_node.neighbors.append(clone_neighbor)
          queue.appendleft(neighbor)
    return start_node
