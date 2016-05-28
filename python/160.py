#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    length_a = 0
    pointer = headA
    while pointer:
      pointer = pointer.next
      length_a += 1
    length_b = 0
    pointer = headB
    while pointer:
      pointer = pointer.next
      length_b += 1
    for i in range(length_a - length_b):
      headA = headA.next
    for i in range(length_b - length_a):
      headB = headB.next
    while headA != headB:
      headA = headA.next
      headB = headB.next
    return headA

a1 = ListNode(0)
a2 = ListNode(0)
b1 = ListNode(0)
b2 = ListNode(0)
b3 = ListNode(0)
c1 = ListNode(0)
c2 = ListNode(0)
c3 = ListNode(0)
a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
b1.next = b2
b2.next = b3
b3.next = c1
s = Solution()
assert (s.getIntersectionNode(a1, b1) == c1)