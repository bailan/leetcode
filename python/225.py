"""
225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
"""

"""
Two queue

1 2 3

1
2 
A B
"""

import collections

class Stack(object):
  def __init__(self):
    """
    initialize your data structure here.
    """
    self.in_queue = collections.deque()
    self.out_queue = collections.deque()

  def push(self, x):
    """
    :type x: int
    :rtype: nothing
    """
    self.in_queue.appendleft(x)
    while self.out_queue:
      self.in_queue.appendleft(self.out_queue.pop())
    while self.in_queue:
      self.out_queue.appendleft(self.in_queue.pop())

  def pop(self):
    """
    :rtype: nothing
    """
    return self.out_queue.pop()    

  def top(self):
    """
    :rtype: int
    """
    return self.out_queue[-1]
      
  def empty(self):
    """
    :rtype: bool
    """
    return not self.out_queue