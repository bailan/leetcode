"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def recoverTree(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    def inorder(node, prev, first, second):
      if not node:
        return
      inorder(node.left, prev, first, second)
      if prev[0].val >= node.val:
        if not first[0]:
          first[0] = prev[0]
        second[0] = node
      prev[0] = node
      inorder(node.right, prev, first, second)

    prev = [TreeNode(-sys.maxint)]
    first = [None]
    second = [None]
    inorder(root, prev, first, second)
    first[0].val, second[0].val = second[0].val, first[0].val