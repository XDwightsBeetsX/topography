"""
Map is primary data struct of topography

Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from .Points import Point, PointValue
from .interpolate import inverse_weight
from .utils.plotting import heatmap
from .utils.glob import *


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
    TODO Make cache for different interpolation schemes  
    TODO Find resolution for fractional matrix sizes
    """
    def __init__(self, rawPoints):
        """
        `RawPoints` is the list of known Points
        """
        self.RawPoints = rawPoints
        self.Cache = {}  # {'type': matrix}
        
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
    
    def showRawPointValues(self):
        """
        Prints Points in `self.RawPoints`
        """
        for pt in self.RawPoints:
            print(f"[{pt.X}, {pt.Y}] {pt.Z}")
    
    def showFilledPointValues(self):
        """
        Prints Points in `self.PointsFilled`
        """
        for row in self.Cache[self.Cache.keys()[0]]:
            for val in row:
                print(f"{val}", end=",")
            print()
    
    def writeFilledPointValuesToCsv(self, request, filename, writeAsMatrix=False):
        """
        Writes series of PointValues in format:  
            x, y, z
        
        Can toggle `writeAsMatrix` to ouput in matrix format
        """
        if request not in self.Cache.keys():
            raise Exception(f"Request <{request}> not found in the Map cache")
        with open(filename + ".csv", "w") as f:
            matrix = self.Cache[request]
            if writeAsMatrix:
                for row in matrix:
                    for pt in row:
                        f.write(pt.Z + ",")
                    f.write('\n')
            else:
                header = "x,y,z\n"
                f.write(header)
                for row in matrix:
                    for pt in row:
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

        # interpolate the points by idw
        height = len(matrix)
        width = len(matrix[0])
        for row in range(height):
            for col in range(width):
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
        
        # save to cache
        self.Cache[IDW] = matrix

        # show plot of interpolated values
        if showWhenDone:
            heatmap(matrix)

    def nn(self, filename="nn"):
        pass

    def linear(self, filename="linear"):
        pass
