



class Point(object):
    def __init__(self, x, y, value):
        self.X = x
        self.Y = y
        self.Value = value
    
    def show(self):
        print(f"[{self.X}, {self.Y}]: {self.Value}")
