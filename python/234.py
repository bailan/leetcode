"""
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
"""

"""
Find the middle node, reverse the later half, then compare
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def isPalindrome(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    middle = self.find_middle_node(head)
    middle = self.reverse(middle)
    if not middle:
      return True
    middle = middle.next
    while middle:
      if head.val != middle.val:
        return False
      head = head.next
      middle = middle.next
    return True

  def find_middle_node(self, head):
    if not head:
      return None
    slow = head
    fast = head.next
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
    return slow

  def reverse(self, node):
    if not node or not node.next:
      return node
    current = node.next
    next = current.next
    current.next = None
    while next:
      temp = next.next
      next.next = current
      current = next
      next = temp
    node.next = current
    return node

s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(1)
node1.next = node2
node2.next = node3
assert (s.isPalindrome(node1))
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
assert (s.isPalindrome(node1) == False)
node1 = ListNode(1)
assert (s.isPalindrome(node1))