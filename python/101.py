"""
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def is_symmetric(left, right):
      if not left and not right:
        return True
      if (not left and right) or (left and not right):
        return False
      if left.val != right.val:
        return False
      return is_symmetric(left.left, right.right) and is_symmetric(left.right, right.left)

    if not root:
      return True
    return is_symmetric(root.left, root.right)