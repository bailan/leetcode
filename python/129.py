"""
129. Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sumNumbers(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    return self.dfs(root, 0)
  
  def dfs(self, node, current):
    if not node:
      return 0
    current = current * 10 + node.val
    if not node.left and not node.right:
      return current
    return self.dfs(node.left, current) + self.dfs(node.right, current)