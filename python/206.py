"""
206. Reverse Linked List

Reverse a singly linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    tail = None
    while head:
      head.next, tail, head = tail, head, head.next
    return tail