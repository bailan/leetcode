"""
227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
"""

class Solution(object):
  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    op_stack = []
    value_stack = []
    i, n = 0, len(s)
    while i < n:
      c = s[i]
      if c.isdigit():
        value = int(c)
        while i + 1 < n and s[i + 1].isdigit():
          i += 1
          value = value * 10 + int(s[i])
        value_stack.append(value)
      elif c in '+-*/':
        while op_stack and self.precedence(op_stack[-1], c):
          self.operate(op_stack, value_stack)
        op_stack.append(c)
      i += 1
    while op_stack:
      self.operate(op_stack, value_stack)
    return value_stack.pop()

  def precedence(self, op1, op2):
    return op1 in '*/' or op2 in '+-'

  def operate(self, op_stack, value_stack):
    b = value_stack.pop()
    a = value_stack.pop()
    op = op_stack.pop()
    if op == '+':
      value_stack.append(a + b)
    elif op == '-':
      value_stack.append(a - b)
    elif op == '*':
      value_stack.append(a * b)
    elif op == '/':
      value_stack.append(a / b)

s = Solution()
assert (s.calculate("3+2*2") == 7)
assert (s.calculate(" 3/2 ") == 1)
assert (s.calculate(" 3+5 / 2 ") == 5)