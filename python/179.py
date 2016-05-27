"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
  # @param {integer[]} nums
  # @return {string}
  def largestNumber(self, nums):
    string_nums = [str(num) for num in nums]
    result = sorted(string_nums, cmp=lambda x,y: cmp(x+y, y+x))
    while len(result) > 1 and result[-1] == '0':
      result.pop()
    return ''.join(reversed(result))

s = Solution()
print s.largestNumber([3, 30, 34, 5, 9])
print s.largestNumber([0, 0])