"""
86. Partition List My Submissions QuestionEditorial Solution
Total Accepted: 67500 Total Submissions: 226716 Difficulty: Medium
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def partition(self, head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    small_head = small_tail = ListNode(0)
    large_head = large_tail = ListNode(0)
    while head:
      next_ = head.next
      if head.val < x:
        small_tail.next = head
        small_tail = small_tail.next
        small_tail.next = None
      else:
        large_tail.next = head
        large_tail = large_tail.next
        large_tail.next = None
      head = next_
    small_tail.next = large_head.next
    return small_head.next