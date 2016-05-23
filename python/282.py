"""
282. Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""

"""
dfs: remember last multiple, last value before multiplication
"""

class Solution(object):
  def addOperators(self, num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    result = []
    self.dfs(num, target, result, "", 0, 0, 0, 0)
    return result

  def dfs(self, num, target, result, expression, start_index, value, last_multiple, last_value):
    if start_index == len(num):
      if value == target:
        result.append(expression)
      return
    for i in range(start_index, len(num)):
      number_string = num[start_index:i + 1]
      number = int(number_string)
      if start_index:
        self.dfs(num, target, result, expression + '+' + number_string, i + 1, value + number, number, value)
        self.dfs(num, target, result, expression + '-' + number_string, i + 1, value - number, -number, value)
        self.dfs(num, target, result, expression + '*' + number_string, i + 1, last_value + last_multiple * number, last_multiple * number, last_value)
      else:
        self.dfs(num, target, result, number_string, i + 1, value + number, number, value)
      if number == 0:
        break

s = Solution()
assert (set(s.addOperators("123", 6)) == set(["1+2+3", "1*2*3"]))
assert (set(s.addOperators("232", 8)) == set(["2*3+2", "2+3*2"]))
assert (set(s.addOperators("105", 5)) == set(["1*0+5","10-5"]))
assert (set(s.addOperators("00", 0)) == set(["0+0", "0-0", "0*0"]))
assert (set(s.addOperators("3456237490", 9191)) == set([]))