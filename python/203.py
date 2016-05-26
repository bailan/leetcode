"""
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

"""
Recursion O(n) stack space
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    while head and head.val == val:
      head = head.next
    if not head:
      return None
    previous = head
    current = head.next
    while current:
      if current.val == val:
        previous.next = current.next
      else:
        previous = current
      current = current.next
    return head