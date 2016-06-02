"""
118. Pascal's Triangle My Submissions QuestionEditorial Solution
Total Accepted: 85796 Total Submissions: 253845 Difficulty: Easy
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if not numRows:
      return []
    result = [[1]]
    for i in range(1, numRows):
      row = [1]
      for j in range(1, i):
        row.append(result[i - 1][j - 1] + result[i - 1][j])
      row.append(1)
      result.append(row)
    return result