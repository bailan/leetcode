"""
107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def levelOrderBottom(self, root):
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
    return result[::-1]