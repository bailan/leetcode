"""
165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""

class Solution(object):
  def compareVersion(self, version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    list1 = [int(number) for number in version1.split('.')]
    list2 = [int(number) for number in version2.split('.')]
    list1.extend([0] * (len(list2) - len(list1)))
    list2.extend([0] * (len(list1) - len(list2)))
    return cmp(list1, list2)

s = Solution()
assert (s.compareVersion("0.1", "1.1") == -1)
assert (s.compareVersion("1.1", "1.2") == -1)
assert (s.compareVersion("1.2", "13.13") == -1)
assert (s.compareVersion("1.0", "1.0.0") == 0)