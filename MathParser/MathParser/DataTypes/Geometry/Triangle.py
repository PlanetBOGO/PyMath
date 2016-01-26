from Point import Point
from Line import Line
class Triangle(object):
    """Triangle represented by three lines and three angles"""
    data = {}
    def __init__(self, data):
        """data = [{"a": [angle, line]},{"b": [angle, line]}, {"c", [angle,line]}"""
        for x in data: 
            self.data.update(x)
