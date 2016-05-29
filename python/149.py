"""
149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""

"""
fix a point and group other points on line with respect to the fixed point. 
"""

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
  def maxPoints(self, points):
    """
    :type points: List[Point]
    :rtype: int
    """
    n = len(points)
    max_number = 0
    for i in range(n):
      vertical = 0
      coincident = 0
      slopes = {}
      max_number_of_same_slope = 0
      for j in range(i + 1, n):
        if points[i].x == points[j].x:
          if points[i].y == points[j].y:
            coincident += 1
          else:
            vertical += 1
        else:
          slope = float(points[i].y - points[j].y) / (points[i].x - points[j].x)
          if slope not in slopes:
            slopes[slope] = 1
          else:
            slopes[slope] += 1
          max_number_of_same_slope = max(max_number_of_same_slope, slopes[slope])
      max_number = max(max_number, 1 + coincident + max(max_number_of_same_slope, vertical))
    return max_number