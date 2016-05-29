"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""

"""
-1/2 = 0!
"""

class Solution(object):
  def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    value_stack = []
    for token in tokens:
      if token in '+-*/':
        b = value_stack.pop()
        a = value_stack.pop()
        if token == '+':
          value_stack.append(a + b)
        elif token == '-':
          value_stack.append(a - b)
        elif token == '*':
          value_stack.append(a * b)
        else:
          value_stack.append(int(float(a) / b))
      else:
        value_stack.append(int(token))
    return value_stack[-1]

s = Solution()
assert (s.evalRPN(["2", "1", "+", "3", "*"]) == 9)
assert (s.evalRPN(["4", "13", "5", "/", "+"]) == 6)
assert (s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)