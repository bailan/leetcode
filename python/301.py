"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""

"""
So tricky!
If find unmatched parentheses, remove one and recursely process the string 
"""

class Solution(object):
  def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    self.result = []
    self.remove_parentheses(s, 0, 0, '()')
    return self.result
  
  def remove_parentheses(self, s, index_i, index_j, parentheses):
    length = len(s)
    num_par = 0
    for i in range(index_i, length):
      if s[i] == parentheses[0]:
        num_par += 1
      elif s[i] == parentheses[1]:
        num_par -= 1
      if num_par < 0:
        for j in range(index_j, i + 1):
          if s[j] == parentheses[1] and (j == index_j or s[j - 1] != parentheses[1]):
            self.remove_parentheses(s[:j] + s[j+1:], i, j, parentheses)
        return
    if parentheses == '()':
      if num_par > 0:
        self.remove_parentheses(s[::-1], 0, 0, parentheses[::-1])
      else:
        self.result.append(s)   
    else:
      self.result.append(s[::-1])

s = Solution()
assert (set(s.removeInvalidParentheses("()())()")) == set(["()()()", "(())()"]))
assert (set(s.removeInvalidParentheses("(a)())()")) == set(["(a)()()", "(a())()"]))
assert (set(s.removeInvalidParentheses(")(")) == set([""]))
assert (set(s.removeInvalidParentheses("(")) == set([""]))
assert (set(s.removeInvalidParentheses(")")) == set([""]))
assert (set(s.removeInvalidParentheses("())(()")) == set(["()()"]))
assert (set(s.removeInvalidParentheses("((()")) == set(["()"]))
assert (set(s.removeInvalidParentheses("())r)")) == set(["(r)", "()r"]))