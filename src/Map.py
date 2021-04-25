"""
Map is primary data struct of topography
Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""


from .Point import Point


class Map(object):
    """
    initialize with list of known points and optionally the size of desired map output  

        - Read points from csv  
        - Print points to csv  
        - Output map image
    """
    def __init__(self, rawData):
        """
        rawData is list of known Points  
        optional parameters used to determine desired ouput Map size
        """
        self.RawData = rawData
        
        # get min/max points of rawData
        self.xMin, self.xMax = rawData[0].X, rawData[0].X
        self.yMin, self.yMax = rawData[0].Y, rawData[0].Y
        for pt in rawData:
            x, y = pt.X, pt.Y            
            if x < self.xMin:
                self.xMin = x
            elif self.xMax < x:
                self.xMax = x
            elif y < self.yMin:
                self.yMin = y
            elif self.yMax < y:
                self.yMax = y
    
    def readFromCsv(self, filename):
        """
        Reads points in from csv in the form:  
            x,y,value
        """
        try:
            with open(filename, 'r+') as f:
                points = []
                for line in f.readlines():
                    l = line.split(',')
                    
                    # TODO read in as double/floats?
                    x = int(l[0])
                    y = int(l[1])
                    val = float(l[2])
                    
                    p = Point(x, y, val)
                    points.append(p)
                self.RawData = points
        except Exception:
            print(f"[MAP]-[readFromCsv]-[ERROR]-could not read points from file '{filename}'")            
    
    def addPoint(self, newPt):
        self.RawData.append(newPt)
    
    def show(self):
        for pt in self.RawData:
            print(f"[{pt.X}, {pt.Y}] {pt.Value}")
