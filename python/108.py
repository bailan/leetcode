"""
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def bst(array, left, right):
      if left == right:
        return None
      mid = (left + right) / 2
      node = TreeNode(array[mid])
      node.left = bst(array, left, mid)
      node.right = bst(array, mid + 1, right)
      return node
      
    if not nums:
      return None
    return bst(nums, 0, len(nums))