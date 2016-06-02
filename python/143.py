"""
143. Reorder List

Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def reorderList(self, head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if not head:
      return head
    middle = self.get_middle_node(head)
    next_ = middle.next
    middle.next, middle = None, middle.next
    self.interlace(head, middle)
    return head
  
  def get_middle_node(self, node):
    if not node or not node.next:
      return node
    slow = node
    fast = node.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

  def reverse(self, node):
    prev = None
    while node:
      next_ = node.next
      node.next = prev
      prev = node
      node = next_
    return prev

  def interlace(self, node1, node2):
    while node2:
      next1 = node1.next
      next2 = node2.next
      node1.next = node2
      node2.next = next1
      node1 = next1
      node2 = next2

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
s = Solution()
s.reorderList(node1)