"""
Map is primary data struct of topography

Stores known points, and allows for performing various interpolation schemes on the raw data.  
"""

from .Points import Point, PointValue
from .interpolate import inverse_weight
from .utils.glob import EMPTY

from matplotlib import pyplot as plt


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
    """
    def __init__(self, rawPoints):
        """
        `RawPoints` is the list of known Points
        """
        self.RawPoints = rawPoints
        
        self.FilledX = []
        self.FilledY = []
        self.FilledZ = []
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
        """
        Clears the last filled matrix and points list.
        """
        self.FilledX.clear()
        self.FilledY.clear()
        self.FilledZ.clear()
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
    
    def showPlot(self, title="Interpolated Topography"):
        """
        Makes a heatmap and a surface plot of the last executed interpolation.  
        Typically called after running an interpolation with `showWhenDone=True`.

        For more colormaps, see https://matplotlib.org/stable/tutorials/colors/colormaps.html
        """
        # width, height of the figure
        w, h = 10, 5

        # These control colorbar scaling and work magically
        frac, pad = 0.0458, 0.04
        
        fig = plt.figure()
        fig.set_size_inches(w, h)
        fig.suptitle(title, fontsize=18)
        
        cmHeat = plt.get_cmap("viridis")
        cmTerra = plt.get_cmap("terrain")
        
        axHeat = fig.add_subplot(1, 2, 1)
        im = axHeat.imshow(self.FilledMatrix, origin="lower", cmap=cmHeat)
        fig.colorbar(im, ax=[axHeat], location="right", fraction=frac, pad=pad)

        axSurf = fig.add_subplot(1, 2, 2, projection="3d")
        axSurf.plot_trisurf(self.FilledX, self.FilledY, self.FilledZ, cmap=cmTerra, linewidth=0)

        plt.show()

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
        Performs Inverse Distance Weighted interpolation.  
        Can toggle `showWhenDone` to disable map output.
        """
        matrix = self.getEmptyMatrixFromRawPoints()
        pts = []

        w = len(matrix)
        h = len(matrix[0])
        # interpolate the points by idw
        for row in range(w):
            for col in range(h):
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

                    self.FilledX.append(row)
                    self.FilledY.append(col)
                    self.FilledZ.append(newWt)
                    pts.append(newPt)
                    matrix[row][col] = newWt
        
        # save to cache
        self.FilledPoints = pts
        self.FilledMatrix = matrix

        # show plot of interpolated values
        if showWhenDone:
            self.showPlot(title=f"Inverse Distance Interpolation of {w-1}x{h-1} Map")

    def nn(self, filename="nn"):
        pass

    def linear(self, filename="linear"):
        pass
