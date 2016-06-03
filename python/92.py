"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def reverseBetween(self, head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    prev = None
    current = head
    for i in range(1, m):
      prev = current
      current = current.next

    begin = None
    end = current
    for i in range(m, n + 1):
      next_ = current.next
      current.next = begin
      begin = current
      current = next_
    end.next = current
    if prev:
      prev.next = begin
      return head
    else:
      return begin
