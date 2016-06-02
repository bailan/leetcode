"""
117. Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
  def connect(self, root):
    """
    :type root: TreeLinkNode
    :rtype: nothing
    """
    if root:
      if root.left:
        if root.right:
          root.left.next = root.right
        else:
          root.left.next = self.get_next(root)
      if root.right:
        root.right.next = self.get_next(root)
      self.connect(root.right)
      self.connect(root.left)

  def get_next(self, node):
    while node.next:
      node = node.next
      if node.left:
        return node.left
      if node.right:
        return node.right
    return None