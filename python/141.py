"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head:
      return False
    slow = head
    fast = head.next
    while slow != fast:
      if fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      else:
        return False
    return True