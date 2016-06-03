"""
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
      return []
    result = []
    current_nodes = [root]
    while current_nodes:
      current_level = []
      next_nodes = []
      for node in current_nodes:
        current_level.append(node.val)
        if node.left:
          next_nodes.append(node.left)
        if node.right:
          next_nodes.append(node.right)
      result.append(current_level)
      current_nodes = next_nodes
    return result