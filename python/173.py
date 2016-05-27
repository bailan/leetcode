"""
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


# Definition for a  binary tree node
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class BSTIterator(object):
  def __init__(self, root):
    """
    :type root: TreeNode
    """
    self.stack = [None]
    self.push_left(root, self.stack)

  def push_left(self, node, stack):
    while node:
      stack.append(node)
      node = node.left

  def hasNext(self):
    """
    :rtype: bool
    """
    return bool(self.stack[-1])

  def next(self):
    """
    :rtype: int
    """
    node = self.stack.pop()
    self.push_left(node.right, self.stack)
    return node.val

node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)
node4 = TreeNode(0)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(9)
node8 = TreeNode(3)
node9 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.left = node8
node5.right = node9
# Your BSTIterator will be called like this:
i, v = BSTIterator(node1), []
while i.hasNext():
  v.append(i.next())
print v
