"""
Low level data structure for euclidian point-values
"""


class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def getString(self):
        return f"[{self.X}, {self.Y}]"


class PointValue(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.Z = z
    
    def getString(self):
        return f"[{self.X}, {self.Y}]: {self.Z}"
