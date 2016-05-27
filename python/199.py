"""
199. Binary Tree Right Side View

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def rightSideView(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    self.right_side_view(root, 0, result)
    return result
  
  def right_side_view(self, root, level, result):
    if not root:
      return
    if len(result) <= level:
      result.append(root.val)
    self.right_side_view(root.right, level + 1, result)
    self.right_side_view(root.left, level + 1, result)