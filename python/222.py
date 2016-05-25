"""
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def countNodes(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root:
      left = self.left_length(root.left)
      right = self.right_length(root.right)
      if left == right:
        return (2 << left) - 1
      else:
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
    return 0 

  def left_length(self, root):
    if root:
      return self.left_length(root.left) + 1
    return 0

  def right_length(self, root):
    if root:
      return self.right_length(root.right) + 1
    return 0

"""
       1
   2       3
 4   5   6   7
8 9
"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node9 = TreeNode(9)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node8
node4.right = node9
s = Solution()
assert (s.countNodes(node1) == 9)
assert (s.countNodes(node2) == 5)
assert (s.countNodes(node8) == 1)