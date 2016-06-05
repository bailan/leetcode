"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""

class Solution(object):
  def simplifyPath(self, path):
    """
    :type path: str
    :rtype: str
    """
    stack = []
    for folder in path.strip('/').split('/'):
      if not folder or folder == '.':
        continue
      elif folder == '..':
        if stack:
          stack.pop()
      else:
        stack.append(folder)
    return '/' + '/'.join(stack)

s = Solution()
assert (s.simplifyPath("/home/") == "/home")
assert (s.simplifyPath("/a/./b/../../c/") == "/c")
assert (s.simplifyPath("/.") == "/")
assert (s.simplifyPath("/./") == "/")
assert (s.simplifyPath("/a/../") == "/")
assert (s.simplifyPath("/a//../") == "/")
assert (s.simplifyPath("/..") == "/")