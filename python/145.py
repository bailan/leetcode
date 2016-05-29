"""
145. Binary Tree Postorder Traversal My Submissions QuestionEditorial Solution
Total Accepted: 99048 Total Submissions: 276965 Difficulty: Hard
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].
"""

"""
Postorder traversal is the reverse of preorder(root, right, left) traversal
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
      return []
    result = []
    stack = [root]
    while stack:
      node = stack.pop()
      result.append(node)
      if node.left:
        stack.append(node.left)
      if node.right:
        stack.append(node.right)
    return result[::-1]