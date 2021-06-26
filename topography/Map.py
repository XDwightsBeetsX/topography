"""
Map is primary data struct of topography

Stores known PointValues, and allows for performing various interpolation schemes on the raw data.  
"""

from .Points import PointValue
from .interpolate import inverse_weight, nearest_neighbor

from matplotlib import pyplot as plt


class Map(object):
    """
    initialize with list of known PointValues
        - Read PointValues from csv  
        - Print PointValues to csv  
        - Output map image
    
    Uses inverted y-axis convention for easier plotting:  
        [[ x1y4, None, None],
         [ None, x2y3, None],
         [ None, None, None],
         [ None, None, x3y1]]
    """
    def __init__(self, rawPointValues, xRange=None, yRange=None):
        """
        `rawPointValues` is the list of known PointValues
        
        Optionally, specify a tuple of (min, max) for `xRange` and `yRange`
        """
        def getXYRange(pointValues):
            """
            Returns an `xRange` and `yRange` in tuples for a set of input PointValues
            """
            xMin, xMax = pointValues[0].X, pointValues[0].X
            yMin, yMax = pointValues[0].Y, pointValues[0].Y
            for pt in pointValues:
                x, y = pt.X, pt.Y
                if x < xMin:
                    xMin = x
                elif xMax < x:
                    xMax = x
                if y < yMin:
                    yMin = y
                elif yMax < y:
                    yMax = y
            return (xMin, xMax), (yMin, yMax)
        
        self.RawPointValues = rawPointValues
        self.FilledX = []
        self.FilledY = []
        self.FilledZ = []
        self.FilledPointValues = []

        # Set x and y ranges
        hasXr = xRange != None
        hasYr = yRange != None
        if hasXr and hasYr:
            self.XRange = xRange
            self.YRange = yRange
        else:
            if hasXr:
                self.XRange = xRange
                self.YRange = getXYRange(rawPointValues)[1]
            elif hasYr:
                self.XRange = self.YRange = getXYRange(rawPointValues)[0]
                self.YRange = yRange
            else:
                xR, yR = getXYRange(rawPointValues)
                self.XRange = xR
                self.YRange = yR
    
    def addPointValue(self, newPointValue):
        """
        Directly adds a PointValue to `self.RawPointValues`
        """
        self.RawPointValues.append(newPointValue)
    
    def clearLast(self):
        """
        Clears the last `FilledPointValues` list and the `Filled X, Y, and Z` 1d lists
        """
        self.FilledX.clear()
        self.FilledY.clear()
        self.FilledZ.clear()
        self.FilledPointValues.clear()
    
    def getFilledPointValue(self, x, y):
        """
        Attempts to find a PointValue in `self.FilledPointValues`

        Throws Exception if not found
        """
        for pt in self.FilledPointValues:
            if pt.X == x and pt.Y == y:
                return pt
        raise Exception(f"PointValue not found at [{x}, {y}]")

    def getAsMatrix(self):
        """
        Returns a 2-D matrix of FilledPointValues Z-values
        """
        matrix = []
        for y in range(self.YRange[0], self.YRange[1]):
            row = []
            for x in range(self.XRange[0], self.XRange[1]):
                row.append(self.getFilledPointValue(x, y).Z)
            matrix.append(row)
        return matrix

    def showRawPointValues(self):
        """
        Prints PointValues in `self.RawPointValues`
        """
        for pt in self.RawPointValues:
            print(pt.getString())
    
    def showFilledPointValues(self):
        """
        Prints PointValues in `self.PointValuesFilled`
        """
        for pt in self.FilledPointValues:
            print(pt.getString())
    
    def writeLastToCsv(self, filename, writeAsMatrix=False):
        """
        Writes series of PointValues in format:  
            x, y, z  
        Can toggle `writeAsMatrix` to ouput in matrix format
        """
        with open(filename + ".csv", "w") as f:
            matrix = self.getAsMatrix()
            if writeAsMatrix:
                for row in matrix:
                    for pt in row:
                        f.write(f"{pt},")
                    f.write('\n')
            else:
                header = "x,y,z\n"
                f.write(header)
                for pt in self.FilledPointValues:
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
        heatMatrix = self.getAsMatrix()
        im = axHeat.imshow(heatMatrix, origin="lower", cmap=cmHeat)
        fig.colorbar(im, ax=[axHeat], location="right", fraction=frac, pad=pad)

        axSurf = fig.add_subplot(1, 2, 2, projection="3d")
        axSurf.plot_trisurf(self.FilledX, self.FilledY, self.FilledZ, cmap=cmTerra, linewidth=0)

        plt.show()

    def idw(self, showWhenDone=True):
        """
        Performs Inverse Distance Weighted interpolation.  
        Can toggle `showWhenDone` to disable map output.
        """
        plot_title = "Inverse Distance Map Interpolation"
        pts = []

        # interpolate the PointValues by idw
        for y in range(self.YRange[0], self.YRange[1]):
            for x in range(self.XRange[0], self.XRange[1]):
                newPt = PointValue(x, y, 0)
                newWt = 0
                totWeight = 0
                for rawPt in self.RawPointValues:
                    wt = inverse_weight(newPt, rawPt)
                    newWt += rawPt.Z * wt
                    totWeight += wt
                newWt /= totWeight
                newPt.Z = newWt

                self.FilledX.append(x)
                self.FilledY.append(y)
                self.FilledZ.append(newWt)
                pts.append(newPt)
        
        # save to cache
        self.FilledPointValues = pts

        # show plot of interpolated values
        if showWhenDone:
            self.showPlot(title=plot_title)

    def nn(self, showWhenDone=True):
        """
        Performs Nearest Neighbor interpolation.  
        Can toggle `showWhenDone` to disable map output.  

        In the case of ties, an average of the nearest is calculated.      
        """
        plot_title = "Nearest Neighbor Map Interpolation"
        pts = []

        # interpolate the PointValues by nn
        yL, yH = self.YRange[0], self.YRange[1]
        xL, xH = self.XRange[0], self.XRange[1]
        longest = ( (yH - yL)**2 + (xH - xL)**2 ) ** (1/2)
        for y in range(yL, yH):
            for x in range(xL, xH):
                newPt = PointValue(x, y, 0)

                nnVal = nearest_neighbor(newPt, self.RawPointValues, longest)

                newPt.Z = nnVal
                self.FilledX.append(x)
                self.FilledY.append(y)
                self.FilledZ.append(nnVal)
                pts.append(newPt)
        
        # save to cache
        self.FilledPointValues = pts

        # show plot of interpolated values
        if showWhenDone:
            self.showPlot(title=plot_title)
