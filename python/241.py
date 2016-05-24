"""
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""

"""
Recursion
"""

class Solution(object):
  def diffWaysToCompute(self, input):
    """
    :type input: str
    :rtype: List[int]
    """
    n = len(input)
    result = []
    for i in range(n):
      if input[i] in '+-*':
        left = self.diffWaysToCompute(input[:i])
        right = self.diffWaysToCompute(input[i+1:])
        for l in left:
          for r in right:
            if input[i] == '+':
              result.append(l + r)
            elif input[i] == '-':
              result.append(l - r)
            else:
              result.append(l * r)
    if not result:
      return [int(input)]
    return result

s = Solution()
assert (set(s.diffWaysToCompute("2-1-1")) == set([0, 2]))
assert (set(s.diffWaysToCompute("2*3-4*5")) == set([-34, -14, -10, -10, 10]))