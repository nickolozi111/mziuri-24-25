# davaleba 19

# question 1
# class Fraction:
#     def __init__(self, top, bottom):
#         self.top = top
#         self.bottom = bottom
#
#     def __str__(self):
#         return f"{self.top}/{self.bottom}"
#
#     def add(self, other):
#         return Fraction(self.top * other.bottom + self.bottom * other.top, self.bottom * other.bottom)
#
#     def inverse(self):
#         return Fraction(self.bottom, self.top)
#
# fraction1 = Fraction(3, 5)
# fraction2 = Fraction(2, 7)
# print(f"Sum: {fraction1.add(fraction2)}")
# print(f"Inverse of fraction1: {fraction1.inverse()}")

# question 2
import math
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_from_origin(self):
#         return math.sqrt(self.x**2 + self.y**2)
#
# point1 = Point(3, 5)
# print(f"Distance from origin: {point1.distance_from_origin()}")

# question 3
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance_to(self, other):
#         return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
#
# # Example usage
# point1 = Point(3, 5)
# point2 = Point(6, 9)
# print(f"Distance between points: {point1.distance_to(point2)}")

