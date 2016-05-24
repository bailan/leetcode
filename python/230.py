"""
230. Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  
  def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    result = TreeNode(-1)
    self.kth_smallest(root, k, result)
    return result.val

  def kth_smallest(self, node, k, result):
    if not node or k <= 0:
      return 0
    count_left = self.kth_smallest(node.left, k, result)
    if count_left == k - 1:
      result.val = node.val
    count_right = self.kth_smallest(node.right, k - count_left - 1, result)
    return count_left + count_right + 1

node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)
node4 = TreeNode(1)
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
s = Solution()
assert (s.kthSmallest(node1, 1) == 1)
assert (s.kthSmallest(node1, 2) == 2)
assert (s.kthSmallest(node1, 3) == 3)
assert (s.kthSmallest(node1, 4) == 4)