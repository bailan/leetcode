"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
  def copyRandomList(self, head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    if not head:
      return None
    self.interlace(head)
    self.connect_random(head)
    return self.separate(head)

  def interlace(self, head):
    while head:
      next_ = head.next
      node = RandomListNode(head.label)
      head.next = node
      node.next = next_
      head = next_

  def connect_random(self, head):
    while head:
      if head.random:
        head.next.random = head.random.next
      head = head.next.next

  def separate(self, head):
    separate_head = head.next
    while head.next.next:
      next_ = head.next.next
      if next_:
        head.next.next = next_.next
      head.next.next = next_.next
      head.next = next_
      head = next_
    return separate_head