"""
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution(object):
  def restoreIpAddresses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    def valid_number(s):
      return s and 0 <= int(s) <= 255 and str(int(s)) == s

    def dfs(s, index, ip, result):
      if len(ip) == 3:
        if valid_number(s[index:]):
          result.append('.'.join(ip + [s[index:]]))
        return
      for i in range(index + 1, min(index + 4, len(s))):
        if valid_number(s[index:i]):
          dfs(s, i, ip + [s[index:i]], result)

    result = []
    dfs(s, 0, [], result)
    return result

s = Solution()
print s.restoreIpAddresses("25525511135")