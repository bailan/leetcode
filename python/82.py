"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev_head = ListNode(0)
    prev_head.next = head
    prev = prev_head
    current = head
    while current:
      if current.next and current.val == current.next.val:
        while current.next and current.val == current.next.val:
          current = current.next
        prev.next = current.next
        current = current.next
      else:
        prev = current
        current = current.next
    return prev_head.next
