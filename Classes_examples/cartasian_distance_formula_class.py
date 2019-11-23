import math

class Point(object):
   def __init__(self, x_param = 1.0, y_param = 2.0):
      self.x = x_param
      self.y = y_param

   def distance(self, parameter_point):
      """Disctance between self and point"""
      x_diff = self.x - parameter_point.x #(x1-x2)
      y_diff = self.y - parameter_point.y  #(y1-y2)

      return math.sqrt(x_diff**2 + y_diff**2)

   def sum(self, parameter_point):
      """Verctor sum of self and point"""
      new_point = Point()
      new_point.x = self.x + parameter_point.x #calculate x value sum from self and point
      new_point.y = self.y + parameter_point.y
      return new_point


def main():
   p1 = Point(2.1, 4.1)
   p2 = Point()
   p3 = p1.sum(p2)

   print(p1.x, p1.y)
   print(p2.x, p2.y)
   print()
   print(p1.distance(p2))
   print()
   print(p3.x, p3.y)


main()