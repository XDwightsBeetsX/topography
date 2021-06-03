"""
Map is primary data struct of topography
Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from matplotlib import pyplot as plt

from Point import Point
from interpolate import euclidian_distance, inverse_weight

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

    TODO Deal with user-input map sizes
    TODO Make cache for different interpolation schemes
    """
    def __init__(self, rawData):
        """
        `rawData` is list of known Points  
        
        TODO optional parameters used to determine desired ouput Map size
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
            if y < self.yMin:
                self.yMin = y
            elif self.yMax < y:
                self.yMax = y          
    
    def addPoint(self, newPt):
        """
        Directly adds a Point to `self.RawData`
        """
        self.RawData.append(newPt)
    
    def show(self):
        """
        Prints Points in `self.RawData`
        """
        for pt in self.RawData:
            print(f"[{pt.X}, {pt.Y}] {pt.Value}")
    
    def getEmptyPoints(self):
        """
        Returns a list of all Points where `pt.Values` are `None`
        """
        def isFilledAt(x, y):
            """
            If a Point is filled, returns `True` and the `Point`  
            Otherwise just returns `False` and `None`
            """
            for pt in self.RawData:
                if pt.X == x and pt.Y == y:
                    if pt.Value != None:
                        return (True, pt)
            return (False, None)
        
        pts = []
        for y in range(self.yMin, self.yMax + 1):
            for x in range(self.xMin, self.xMax + 1):
                filled = isFilledAt(x, y)
                if filled[0]:
                    pts.append(filled[1])
                else:
                    pts.append(Point(x, y, None))
        
        return pts

    def makeMatrix(self, pts):
        """
        Requires a complete set of points  
        
        Returns a 2-D matrix of values
        """
        m = []
        for y in range(self.yMin, self.yMax + 1):
            r = []
            for x in range(self.xMin, self.xMax + 1):
                for pt in pts:
                    if pt.X == x and pt.Y == y:
                        r.append(pt.Value)
            m.append(r)
        return m

    def readFromCsv(self, filename):
        """
        Reads points in from csv in the form:  
            x, y, z(value)
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
    
    def writeToCsv(self, pts, filename, writeAsMatrix=False):
        """
        Writes series of points in format:  
            x, y, z (value)
        
        Can toggle `writeAsMatrix` to ouput a matrix.
        """
        if writeAsMatrix:
            # write matrix to csv as map
            m = self.makeMatrix(pts)

            with open(filename + ".csv", "w") as f:
                for row in m:
                    for val in row:
                        f.write(str(val) + ",")
                    f.write('\n')
        else:
            # write matrix to csv as pt-value
            with open(filename + ".csv", "w") as f:
                header = "x,y,z\n"
                f.write(header)
                for pt in pts:
                    f.write(f"{str(pt.X)},{str(pt.Y)},{str(pt.Value)}\n")

    def idw(self, filename="idw", showWhenDone=True, localWeightModifier=1.0):
        """
        Performs Inverse Distance Weighted Interpolation

        Can toggle `showWhenDone` to disable map output.  
        
        `localWeightModifier` should be in domain `[0,1]` and increases dropoff rate of weights.

        TODO Optimize weighting domain by only weighting points within a region
        TODO Optimize weighting exponent (not sure how unless final map is known)
        """
        # get total list of points of interest
        pts = self.getEmptyPoints()

        # interpolate the points by idw
        for pt in pts:
            if pt.Value == None:
                pt.Value = 0
                for rawPt in self.RawData:
                    wt = inverse_weight(pt, rawPt, modifier=localWeightModifier)
                    pt.Value += rawPt.Value * wt
                pt.Value /= len(self.RawData)
        
        # populate matrix by iterating through known Points self.RawData
        m = self.makeMatrix(pts)

        # ouput to file
        self.writeToCsv(pts, filename)

        # show plot of interpolated values
        if showWhenDone:
            plt.imshow(m)
            plt.colorbar()
            plt.show()

    def linear(self, filename="idw", showWhenDone=True):
        """
        Performs Linear Interpolation
        
        Can toggle showWhenDone to disable map output.

        Start with creating a matrix just large enough.
            TODO Deal with user-input map sizes later
            TODO Make cache for different interpolation schemes later
        """
        # get total list of points of interest
        pts = self.getEmptyPoints()

        # perform linear interpolation
        for pt in pts:
            if pt.Value == None:
                pt.Value = 0
                for rawPt in self.RawData:
                    pt.Value += 0 # TODO
                # pt.Value /= len(self.RawData)
        
        # populate matrix by iterating through known Points self.RawData
        m = self.makeMatrix(pts)

        # ouput to file
        self.writeToCsv(pts, filename)

        # show plot of interpolated values
        if showWhenDone:
            plt.imshow(m)
            plt.colorbar()
            plt.show()

