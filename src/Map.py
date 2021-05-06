"""
Map is primary data struct of topography
Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from matplotlib import pyplot as plt

from Point import Point
from interpolate import *

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
    
    def getEmptyPoints(self, filler=None):
        """
        From known points in rawData, returns a list of all points in area with gaps filled in by 'filler'  

        Can specify 'filler'. Default is None.  
            
            TODO optional sizing
        """
        def isFilledAt(x, y, filler):
            for pt in self.RawData:
                if pt.X == x and pt.Y == y:
                    if pt.Value != filler:
                        return (True, pt)
            return (False, None)
        
        pts = []
        for y in range(self.yMin, self.yMax + 1):
            for x in range(self.xMin, self.xMax + 1):
                # check if point in rawData
                filled = isFilledAt(x, y, filler)
                if filled[0]:
                    # make new pt
                    pts.append(filled[1])
                else:
                    pts.append(Point(x, y, filler))
        
        return pts
                
    def idw(self, filler=None):
        """
        Performs Inverse Distance Weighted Interpolation
            Saves a .csv map to file

        Start with creating a matrix just large enough.
            TODO Deal with user-input map sizes later
            TODO Make cache for different interpolation schemes later
        """
        # get total list of points of interest
        pts = self.getEmptyPoints(filler=filler)

        # interpolate the points by idw
        for pt in pts:
            if pt.Value == filler:
                pt.Value = 0
                for raw in self.RawData:
                    pt.Value += raw.Value * inverse_weight(pt, raw)
        
        # populate matrix by iterating through known Points self.RawData
        m = []
        for y in range(self.yMin, self.yMax + 1):
            r = []
            for x in range(self.xMin, self.xMax + 1):
                for pt in pts:
                    if pt.X == x and pt.Y == y:
                        r.append(pt.Value)
                    else:
                        continue
            m.append(r)

        print(m)

        plt.imshow(m)
        plt.show()

        # ouput to file

        # show plot of interpolated values



p1 = Point(1, 1, 100)
p2 = Point(1, 20, 200)
p3 = Point(10, 10, 300)

M = Map([p1, p2, p3])

M.idw()