"""
Map is primary data struct of topography
Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from Point import Point
# from .interpolate import *

class Map(object):
    """
    initialize with list of known Points and optionally the size of desired map output  

        - Read points from csv  
        - Print points to csv  
        - Output map image
    
    Uses inverted y-axis convention for easier plotting:  
        [[ x1y4, None, None],
         [ None, x2y3, None],
         [ None, None, None],
         [ None, None, x3y1]]
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
    
    def getEmptyMap(self, filler=None):
        """
        From known points in rawData, returns a matrix that fits to size all points  

        Can specify a filler that takes the place of point values. Default is None.  
            
            TODO optional sizing
        """
        m = []
        for y in range(self.yMin, self.yMax + 1):
            r = []
            for x in range(self.xMin, self.xMax + 1):
                r.append(filler)
            m.append(r)

        for pt in self.RawData:
            m[self.yMax - pt.Y][pt.X - self.xMin] = pt.Value
        
        return m
                
    def idw(self, filler=None):
        """
        Performs Inverse Distance Weighted Interpolation
            Saves a .csv map to file

        Start with creating a matrix just large enough.
            TODO Deal with user-input map sizes later
            TODO Make cache for different interpolation schemes later
        """
        # create matrix of proper size
        m = self.getEmptyMap(filler=filler)

        # populate matrix by iterating through known Points self.RawData
        for y in range(len(m)):
            for x in range(len(m[0])):
                if m[y][x] == filler:
                    # perform idw
                    for pt in self.RawData:

        
        # ouput to file

        # show plot of interpolated values

        pass



p1 = Point(1, 1, 10)
p2 = Point(1, 5, 20)
p3 = Point(4, 4, 30)

M = Map([p1, p2, p3])

for r in M.getEmptyMap():
    print(r)

M.idw()
