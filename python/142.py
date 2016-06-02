"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""

class Solution(object):
  def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
      return None
    slow = head
    fast = head.next
    while slow != fast:
      if fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      else:
        return None
    slow = head
    fast = fast.next
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return slow
    
