"""
Low level data structure for euclidian point-values
"""


class Point(object):
    def __init__(self, x, y, value):
        self.X = x
        self.Y = y
        self.Value = value
    
    def getString(self):
        return f"[{self.X}, {self.Y}]: {self.Value}"
