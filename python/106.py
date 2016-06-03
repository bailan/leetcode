"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

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
  def buildTree(self, inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    
    def build_tree(inorder, inleft, inright, postorder, postleft, postright):
      if inleft >= inright:
        return None
      root_index = inorder.index(postorder[postright - 1])
      node = TreeNode(postorder[postright - 1])
      node.left = build_tree(inorder, inleft, root_index, postorder, postleft, postleft + root_index - inleft)
      node.right = build_tree(inorder, root_index + 1, inright, postorder, postleft + root_index - inleft, postright -1)
      return node

    if not inorder:
      return None
    return build_tree(inorder, 0, len(inorder), postorder, 0, len(postorder))