
"""
337. House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""

"""
DP:
f(i): the maximum amount of money that the thief robs node i
g(i): the maximum amount of money that the thief does not rob node i
f(i) = g(i.left) + g(i.right) + v[i]
g(i) = f(i.left) + f(i.right)
"""

# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution(object):
  
  def rob(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    self.n = 0
    self.traverse(root)
    self.f = [None] * self.n
    self.g = [None] * self.n
    return max(self.getf(root), self.getg(root))

  def traverse(self, node):
    if node:
      node.num = self.n
      self.n += 1
      self.traverse(node.left)
      self.traverse(node.right)
 
  def getf(self, node):
    if not node:
      return 0
    if self.f[node.num]:
      return self.f[node.num]
    self.f[node.num] = self.getg(node.left) + self.getg(node.right) + node.val
    return self.f[node.num]

  def getg(self, node):
    if not node:
      return 0
    if self.g[node.num]:
      return self.g[node.num]
    self.g[node.num] = max(self.getf(node.left), self.getg(node.left)) \
      + max(self.getf(node.right), self.getg(node.right))
    return self.g[node.num]

s = Solution()
n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(3)
n5 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.right = n4
n3.right = n5
assert (s.rob(n1) == 7)
n1 = TreeNode(3)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(1)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
assert (s.rob(n1) == 9)
n1 = TreeNode(1)
assert (s.rob(n1) == 1)
n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2
assert (s.rob(n1) == 2)
n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(2)
n4 = TreeNode(3)
n1.left = n2
n2.left = n3
n3.left = n4
assert (s.rob(n1) == 7)
n1 = TreeNode(4)
n2 = TreeNode(1)
n3 = TreeNode(2)
n4 = TreeNode(3)
n1.right = n2
n2.right = n3
n3.right = n4
assert (s.rob(n1) == 7)
