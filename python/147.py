"""
147. Insertion Sort List

Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def insertionSortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return head
    insertion_head = ListNode(0)
    insertion_head.next = head
    while head and head.next and head.val < head.next.val:
      head = head.next
    head.next, head = None, head.next
    while head:
      next_ = head.next
      insert = insertion_head
      while insert.next and insert.next.val < head.val:
        insert = insert.next
      head.next = insert.next
      insert.next = head
      head = next_
    return insertion_head.next

node1 = ListNode(3)
node2 = ListNode(5)
node3 = ListNode(1)
node4 = ListNode(2)
node5 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
sorted_list = s.insertionSortList(node1)
pre = sorted_list.val
while sorted_list.next:
  sorted_list = sorted_list.next
  assert (sorted_list.val >= pre)
  pre = sorted_list.val