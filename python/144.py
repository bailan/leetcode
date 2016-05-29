"""
144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    traverse = []
    stack = [root]
    while stack:
      node = stack.pop()
      traverse.append(node.val)
      if node.right
        stack.append(node.right)
      if node.left:        
        stack.append(node.left)
    return traverse
