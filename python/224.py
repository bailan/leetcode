"""
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
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
    n = len(s)
    i = 0
    while i < n:
      c = s[i]
      #print op_stack, value_stack, c
      if c in '0123456789':
        value = int(c)
        while i + 1 < n and s[i + 1] in '0123456789':
          i += 1
          value = value * 10 + int(s[i])
        value_stack.append(value)
      elif c in '+-':
        while op_stack and self.precedence(op_stack[-1], c):
          self.operate(op_stack, value_stack)
        op_stack.append(c)
      elif c == '(':
        op_stack.append(c)
      elif c == ')':
        while op_stack and op_stack[-1] != '(':
          self.operate(op_stack, value_stack)
        op_stack.pop()
      i += 1
    while op_stack:
      self.operate(op_stack, value_stack)
    return value_stack.pop()

  def precedence(self, op1, op2):
    return op1 != '('

  def operate(self, op_stack, value_stack):
    b = value_stack.pop()
    a = value_stack.pop()
    op = op_stack.pop()
    if op == '+':
      value_stack.append(a + b)
    elif op == '-':
      value_stack.append(a - b)

s = Solution()
assert (s.calculate("1 + 1") == 2)
assert (s.calculate(" 2-1 + 2 ") == 3)
assert (s.calculate("(1+(4+5+2)-3)+(6+8)") == 23)
assert (s.calculate("0") == 0)
assert (s.calculate("(10)") == 10)