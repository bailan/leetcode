"""
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
"""

"""
Recursion lca(node) = 
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root or root == p or root == q:
      return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
      return root
    if left:
      return left
    if right:
      return right

node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(2)
node6 = TreeNode(0)
node7 = TreeNode(8)
node8 = TreeNode(7)
node9 = TreeNode(4)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9
s = Solution()
assert (s.lowestCommonAncestor(node1, node2, node3) == node1)
assert (s.lowestCommonAncestor(node1, node2, node5) == node2)