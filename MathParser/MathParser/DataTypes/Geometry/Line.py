import math
from Point import Point
from Fraction import Fraction
class Line(object):
    """Line consisting of start and end points"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def length(self):
        return math.sqrt((self.start.x - self.end.x) ** 2 + (self.start.y - self.end.y) ** 2)
    def midpoint(self):
        return Point((self.start.x + self.end.x) / 2, (self.start.y + self.end.y) / 2)
    def slope(self):
        #Or should I implement slope as fraction?
        return abs((self.end.x - self.start.x) / (self.end.y - self.start.y))
class Eq_Line(object):
    """Line adhering to the formula y=mx+b"""
    def __init__(self, m, b):
        self.slope = m
        self.xint = b
    