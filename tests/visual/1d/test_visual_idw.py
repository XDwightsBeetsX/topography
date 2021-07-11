"""
1d visual inverse distance tests
"""

from topography.Points import PointValue
from topography.interpolate import inverse_weight

import numpy as np
from matplotlib import pyplot as plt

# May want to toggle when running tests
ShowPlots = False

# Use constant for 1d tests
Y = 0

def test_1d_p2():
    title = "Default Test of Current Approach to IDW"
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
        interpVal = inverse_weight(interpolatedPt, rawPts)
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


def test_1d_cliff():
    title = "Default Cliff Test"
    dx = 0.25
    n = 50

    rawPts = []
    rawPts.append(PointValue(0, Y, 2))
    rawPts.append(PointValue(1, Y, 3))
    rawPts.append(PointValue(2, Y, 2))
    rawPts.append(PointValue(3, Y, 3))
    rawPts.append(PointValue(4, Y, 4))
    rawPts.append(PointValue(5, Y, 5))
    rawPts.append(PointValue(5 + dx, Y, 0))
    rawPts.append(PointValue(6, Y, 1))
    
    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    totPts = []

    for x in newXs:
        interpolatedPt = PointValue(x, Y, 0)
        interpVal = inverse_weight(interpolatedPt, rawPts)
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


def test_1d_peak():
    title = "Default Peak Test"
    dx = 0.25
    n = 50

    rawPts = []
    rawPts.append(PointValue(0, Y, 2))
    rawPts.append(PointValue(1, Y, 2))
    rawPts.append(PointValue(2 - dx, Y, 2))
    rawPts.append(PointValue(2 , Y, 7))
    rawPts.append(PointValue(2 + dx, Y, 2))
    rawPts.append(PointValue(3, Y, 2))
    rawPts.append(PointValue(4, Y, 2))

    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    totPts = []

    for x in newXs:
        interpolatedPt = PointValue(x, Y, 0)
        interpVal = inverse_weight(interpolatedPt, rawPts)
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


def test_1d_comparison():
    title = "Comparisons of Power P Across a Set of Points From Shepard's Method"
    n = 50
    p1 = -2
    p2 = 1/2
    p3 = 1
    p4 = 2

    rawPts = []
    rawPts.append(PointValue(1, Y, 2))
    rawPts.append(PointValue(2, Y, 4))
    rawPts.append(PointValue(3, Y, 4))
    rawPts.append(PointValue(4, Y, 2))

    newXs = np.linspace(rawPts[0].X - 1, rawPts[-1].X + 1, n)
    pts_p1 = []
    pts_p2 = []
    pts_p3 = []
    pts_p4 = []

    for x in newXs:
        interpolatedPt_p1 = PointValue(x, Y, 0)
        interpolatedPt_p2 = PointValue(x, Y, 0)
        interpolatedPt_p3 = PointValue(x, Y, 0)
        interpolatedPt_p4 = PointValue(x, Y, 0)

        interpVal1 = inverse_weight(interpolatedPt_p1, rawPts, p=p1)
        interpVal2 = inverse_weight(interpolatedPt_p2, rawPts, p=p2)
        interpVal3 = inverse_weight(interpolatedPt_p3, rawPts, p=p3)
        interpVal4 = inverse_weight(interpolatedPt_p4, rawPts, p=p4)
        
        interpolatedPt_p1.Z = interpVal1
        interpolatedPt_p2.Z = interpVal2
        interpolatedPt_p3.Z = interpVal3
        interpolatedPt_p4.Z = interpVal4
        
        pts_p1.append(interpolatedPt_p1)
        pts_p2.append(interpolatedPt_p2)
        pts_p3.append(interpolatedPt_p3)
        pts_p4.append(interpolatedPt_p4)
    
    if ShowPlots:
        plt.plot([pt.X for pt in rawPts], [pt.Z for pt in rawPts], "ko", label="Raw")
        plt.plot(newXs, [pt.Z for pt in pts_p1], "b", label=f"P = {p1}")
        plt.plot(newXs, [pt.Z for pt in pts_p2], "g", label=f"P = {p2}")
        plt.plot(newXs, [pt.Z for pt in pts_p3], "y", label=f"P = {p3}")
        plt.plot(newXs, [pt.Z for pt in pts_p4], "r", label=f"P = {p4}")
        
        plt.title(title)
        plt.legend(loc="upper left")
        plt.tight_layout()
        plt.show()
 