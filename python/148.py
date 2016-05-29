"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
"""

"""
quick sort
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    return self.quicksort(head)

  def quicksort(self, head):
    if not head:
      return None
    small, equal, large = self.three_way_partition(head)
    small = self.quicksort(small)
    if small:
      head = small
      while small.next:
        small = small.next
      small.next = equal
    else:
      head = equal
    while equal.next:
      equal = equal.next
    equal.next = self.quicksort(large)
    return head

  def three_way_partition(self, head):
    equal = head
    small = large = None
    head = head.next
    equal.next = None
    while head:
      next_node = head.next
      if head.val == equal.val:
        head.next = equal
        equal = head
      elif head.val > equal.val:
        head.next = large
        large = head
      else:
        head.next = small
        small = head
      head = next_node
    return small, equal, large

node1 = ListNode(4)
node2 = ListNode(5)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(1)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
s = Solution()
sorted_list = s.sortList(node1)
pre = sorted_list.val
while sorted_list.next:
  sorted_list = sorted_list.next
  assert (sorted_list.val >= pre)
  pre = sorted_list.val