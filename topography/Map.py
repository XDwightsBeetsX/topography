"""
Map is primary data struct of topography

Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from .Points import Point, PointValue
from .interpolate import inverse_weight
from .utils.plotting import heatmap
from .utils.glob import EMPTY
from .utils.pile import getKeysAsList


class Map(object):
    """
    initialize with list of known Points
        - Read points from csv  
        - Print points to csv  
        - Output map image
    
    Uses inverted y-axis convention for easier plotting:  
        [[ x1y4, None, None],
         [ None, x2y3, None],
         [ None, None, None],
         [ None, None, x3y1]]

    TODO Deal with user-input map sizes  
    TODO Find resolution for fractional matrix sizes
    """
    def __init__(self, rawPoints):
        """
        `RawPoints` is the list of known Points
        """
        self.RawPoints = rawPoints
        self.FilledPoints = []
        self.FilledMatrix = [[]]
        
        # get min/max points of rawData
        self.xMin, self.xMax = rawPoints[0].X, rawPoints[0].X
        self.yMin, self.yMax = rawPoints[0].Y, rawPoints[0].Y
        for pt in rawPoints:
            x, y = pt.X, pt.Y
            if x < self.xMin:
                self.xMin = x
            elif self.xMax < x:
                self.xMax = x
            if y < self.yMin:
                self.yMin = y
            elif self.yMax < y:
                self.yMax = y
    
    def addPointValue(self, newPointValue):
        """
        Directly adds a PointValue to `self.RawPoints`
        """
        self.RawPoints.append(newPointValue)
    
    def clearLast(self):
        self.FilledMatrix.clear()
        self.FilledPoints.clear()
    
    def showRawPointValues(self):
        """
        Prints Points in `self.RawPoints`
        """
        for pt in self.RawPoints:
            print(pt.getString())
    
    def showFilledPointValues(self):
        """
        Prints Points in `self.PointsFilled`
        """
        for pt in self.FilledPoints:
            print(pt.getString())
    
    def writeLastToCsv(self, filename, writeAsMatrix=False):
        """
        Writes series of PointValues in format:  
            x, y, z
        
        Can toggle `writeAsMatrix` to ouput in matrix format
        """
        with open(filename + ".csv", "w") as f:
            matrix = self.FilledMatrix
            if writeAsMatrix:
                for row in matrix:
                    for pt in row:
                        f.write(f"{pt},")
                    f.write('\n')
            else:
                header = "x,y,z\n"
                f.write(header)
                for pt in self.FilledPoints:
                    f.write(f"{str(pt.X)},{str(pt.Y)},{str(pt.Z)}\n")
        
    def getEmptyMatrixFromRawPoints(self):
        """
        Makes a 2d matrix from RawPoints that has gaps filled with globals.EMPTY
        """
        width = self.xMax - self.xMin + 1
        height = self.yMax - self.yMin + 1
        
        # init empty matrix
        matrix = []
        for _row in range(height):
            row = [EMPTY] * width
            matrix.append(row)
        
        # fill w known pts
        for rawPt in self.RawPoints:
            matrix[rawPt.Y][rawPt.X] = rawPt.Z
        
        return matrix

    def idw(self, showWhenDone=True):
        """
        Performs Inverse Distance Weighted interpolation

        Can toggle `showWhenDone` to disable map output
        """
        matrix = self.getEmptyMatrixFromRawPoints()
        pts = []

        # interpolate the points by idw
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == EMPTY:
                    newPt = PointValue(row, col, 0)
                    newWt = 0
                    totWeight = 0
                    for rawPt in self.RawPoints:
                        wt = inverse_weight(newPt, rawPt)
                        newWt += rawPt.Z * wt
                        totWeight += wt
                    newWt /= totWeight
                    newPt.Z = newWt
                    matrix[row][col] = newWt
                    pts.append(newPt)
        
        # save to cache
        self.FilledPoints = pts
        self.FilledMatrix = matrix

        # show plot of interpolated values
        if showWhenDone:
            heatmap(matrix)

    def nn(self, filename="nn"):
        pass

    def linear(self, filename="linear"):
        pass
