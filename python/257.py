"""
257. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    result = []
    self.get_path(root, [], result)
    return result

  def get_path(self, node, path, result):
    if node:
      path.append(node.val)
      if not node.left and not node.right:
        result.append('->'.join(map(str, path)))
      else:
        self.get_path(node.left, path, result)
        self.get_path(node.right, path, result)
      path.pop()

s = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node5 = TreeNode(5)
node1.left = node2
node1.right = node3
node2.right = node5
assert (s.binaryTreePaths(node1) == ["1->2->5", "1->3"])
node1 = TreeNode(1)
assert (s.binaryTreePaths(node1) == ["1"])
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node2.left = node3
assert (s.binaryTreePaths(node1) == ["1->2->3"])
assert (s.binaryTreePaths(None) == [])