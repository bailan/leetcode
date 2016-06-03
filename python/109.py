"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def sortedListToBST(self, head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    def bst(start_node, end_node):
      if start_node == end_node:
        return None
      slow = fast = start_node
      while fast != end_node and fast.next != end_node:
        slow = slow.next
        fast = fast.next.next
      node = TreeNode(slow.val)
      node.left = bst(start_node, slow)
      node.right = bst(slow.next, end_node)
      return node

    return bst(head, None)