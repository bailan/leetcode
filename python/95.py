"""
95. Unique Binary Search Trees II

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def generateTrees(self, n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    def subtree(left, right):
      if left == right:
        return [None]
      tree = []
      for i in range(left, right):
        for left_node in subtree(left, i):
          for right_node in subtree(i + 1, right):
            node = TreeNode(i)
            node.left = left_node
            node.right = right_node
            tree.append(node)
      return tree

    if not n:
      return []
    return subtree(1, n + 1)