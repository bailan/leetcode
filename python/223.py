"""
223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
        C,D
                 G,H
A,B
       E,F
Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""

"""
Math
"""

class Solution(object):
  def computeArea(self, A, B, C, D, E, F, G, H):
    """
    :type A: int
    :type B: int
    :type C: int
    :type D: int
    :type E: int
    :type F: int
    :type G: int
    :type H: int
    :rtype: int
    """
    x1, y1 = max(A, E), max(B, F)
    x2, y2 = min(C, G), min(D, H)
    if x2 > x1 and y2 > y1:
      return (C - A) * (D - B) + (G - E) * (H - F) - (x2 - x1) * (y2 - y1)
    else:
      return (C - A) * (D - B) + (G - E) * (H - F)
