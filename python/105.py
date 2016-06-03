"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def build_tree(preorder, preleft, preright, inorder, inleft, inright):
      if preleft >= preright:
        return None
      node = TreeNode(preorder[preleft])
      root_index = inorder.index(preorder[preleft])
      node.left = build_tree(preorder, preleft + 1, preleft + root_index - inleft + 1, inorder, inleft, root_index)
      node.right = build_tree(preorder, preleft + root_index - inleft + 1, preright, inorder, root_index + 1, inright)
      return node

    if not preorder:
      return None
    return build_tree(preorder, 0, len(preorder), inorder, 0, len(inorder))