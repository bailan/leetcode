"""
354. Russian Doll Envelopes
Hard

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""

"""
[2,3] -> [5,4]
      -> [6,4]
      -> [6,7]
[5,4] -> [6,7]
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        sorted_envelopes = sorted(envelopes, key=lambda envelope: (envelope[0], -envelope[1]))
        smallest_number_for_index = [0]
        for envelope in sorted_envelopes:
            width = envelope[1]
            if width > smallest_number_for_index[-1]:
                smallest_number_for_index.append(width)
            else:
                left, right = 0, len(smallest_number_for_index) - 1
                while left < right:
                    mid = (left + right) / 2
                    if smallest_number_for_index[mid] < width:
                        left = mid + 1
                    else:
                        right = mid - 1
                smallest_number_for_index[left] = width
        return len(smallest_number_for_index) - 1


print Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
print Solution().maxEnvelopes([])
print Solution().maxEnvelopes([[1,1]])
print Solution().maxEnvelopes([[1,1], [2,2]])
print Solution().maxEnvelopes([[1,1], [1,2]])
print Solution().maxEnvelopes([[1,1], [2,3], [3,2], [4,3]])
print Solution().maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]])