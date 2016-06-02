"""
124. Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def maxPathSum(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return self.dfs(root)[1]
  
  def dfs(self, node):
    if not node:
      return 0, -sys.maxint
    left_path, left_sum = self.dfs(node.left)
    right_path, right_sum = self.dfs(node.right)
    return max(0, max(left_path, right_path) + node.val), max(left_sum, right_sum, left_path + right_path + node.val, node.val)