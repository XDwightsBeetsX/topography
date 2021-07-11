"""
1d visual step tests
"""

from topography.Points import PointValue
from topography.interpolate import step

import numpy as np
from matplotlib import pyplot as plt

# May want to toggle when running tests
ShowPlots = False

# Use constant for 1d tests
Y = 0

def test_1d_default():
    title = "Default Test of Current Approach to Step Interpolation"
    n = 50

    rawPts = []
    rawPts.append(PointValue(1, Y, 1))
    rawPts.append(PointValue(2, Y, 2))
    rawPts.append(PointValue(3, Y, 2))
    rawPts.append(PointValue(4, Y, 1))

    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    totPts = []

    for x in newXs:
        interpolatedPt = PointValue(x, Y, 0)
        interpVal = step(interpolatedPt, rawPts)
        interpolatedPt.Z = interpVal
        totPts.append(interpolatedPt)
    
    if ShowPlots:
        plotXs = [pt.X for pt in totPts]
        plotZs = [pt.Z for pt in totPts]
        plt.plot(plotXs, plotZs, "b--", label="Interpolated")
        plt.plot([pt.X for pt in rawPts], [pt.Z for pt in rawPts], "ko", label="Raw")
        
        plt.title(title)
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()


def test_1d_generic():
    title = "Generic Step Interpolation"
    n = 50

    rawPts = []
    rawPts.append(PointValue(1, Y, 5))
    rawPts.append(PointValue(2, Y, 3))
    rawPts.append(PointValue(3, Y, 1))
    rawPts.append(PointValue(4, Y, 3))
    rawPts.append(PointValue(5, Y, 1))
    rawPts.append(PointValue(6, Y, 7))
    rawPts.append(PointValue(9, Y, 4))
    rawPts.append(PointValue(10, Y, 1))

    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    totPts = []

    for x in newXs:
        interpolatedPt = PointValue(x, Y, 0)
        interpVal = step(interpolatedPt, rawPts)
        interpolatedPt.Z = interpVal
        totPts.append(interpolatedPt)
    
    if ShowPlots:
        plotXs = [pt.X for pt in totPts]
        plotZs = [pt.Z for pt in totPts]
        plt.plot(plotXs, plotZs, "b--", label="Interpolated")
        plt.plot([pt.X for pt in rawPts], [pt.Z for pt in rawPts], "ko", label="Raw")
        
        plt.title(title)
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()


def test_1d_sparse():
    title = "Sparse Step Interpolation"
    n = 50

    rawPts = []
    rawPts.append(PointValue(0, Y, 10))
    rawPts.append(PointValue(5, Y, 5))
    rawPts.append(PointValue(10, Y, 1))
    rawPts.append(PointValue(15, Y, 5))
    rawPts.append(PointValue(20, Y, 10))
    

    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    totPts = []

    for x in newXs:
        interpolatedPt = PointValue(x, Y, 0)
        interpVal = step(interpolatedPt, rawPts)
        interpolatedPt.Z = interpVal
        totPts.append(interpolatedPt)
    
    if ShowPlots:
        plotXs = [pt.X for pt in totPts]
        plotZs = [pt.Z for pt in totPts]
        plt.plot(plotXs, plotZs, "b--", label="Interpolated")
        plt.plot([pt.X for pt in rawPts], [pt.Z for pt in rawPts], "ko", label="Raw")
        
        plt.title(title)
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()
