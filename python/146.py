"""
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

class LRUCache(object):

  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity = capacity
    self.size = 0
    self.hashtable = {}
    self.list = DoubleLinkedList()

  def get(self, key):
    """
    :rtype: int
    """
    if key in self.hashtable:
      node = self.hashtable[key]
      self.list.remove(node)
      self.list.appendleft(node)
      return node.val
    else:
      return -1

  def set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    if key in self.hashtable:
      node = self.hashtable[key]
      node.val = value
      self.list.remove(node)
      self.list.appendleft(node)
    else:
      if self.size == self.capacity:
        del self.hashtable[self.list.pop().key]
      else:
        self.size += 1
      node = Node(value, key)
      self.list.appendleft(node)
      self.hashtable[key] = node


class Node(object):
  def __init__(self, value, key):
    self.val = value
    self.key = key
    self.prev = None
    self.next = None

class DoubleLinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def appendleft(self, node):
    if not self.head:
      self.head = self.tail = node
    else:
      self.head.prev = node
      node.next = self.head
      self.head = node

  def pop(self):
    node = self.tail
    if self.tail.prev:
      self.tail = self.tail.prev
      self.tail.next = None
      node.prev = None
    else:
      self.tail = None
    return node

  def remove(self, node):
    if self.head == self.tail:
      self.head = self.tail = None
    elif self.head == node:
      self.head = self.head.next
      self.head.prev = None
    elif self.tail == node:
      self.tail = self.tail.prev
      self.tail.next = None
    else:
      node.prev.next = node.next
      node.next.prev = node.prev

cache = LRUCache(3)
assert (cache.get(0) == -1)
cache.set(0, 0)
assert (cache.get(0) == 0)
cache.set(1, 0)
assert (cache.get(1) == 0)
cache.set(1, 1)
assert (cache.get(1) == 1)
cache.set(2, 2)
assert (cache.get(2) == 2)
cache.set(3, 3)
assert (cache.get(3) == 3)
assert (cache.get(0) == -1)