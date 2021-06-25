"""
interpolate.euclidian_distance tests
"""

from topography.Points import PointValue
from topography.interpolate import inverse_weight, euclidian_distance
from ..msgs import running, passed, failed

import numpy as np
from matplotlib import pyplot as plt

# May want to toggle when running tests
ShowPlots = True

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
        totWt = 0
        newWt = 0
        interpolatedPt = PointValue(x, Y, newWt)
        for rPt in rawPts:
            wt = inverse_weight(interpolatedPt, rPt)
            newWt += rPt.Z * wt
            totWt += wt
        newWt /= totWt
        interpolatedPt.Z = newWt
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
        totWt = 0
        newWt = 0
        interpolatedPt = PointValue(x, Y, newWt)
        for rPt in rawPts:
            wt = inverse_weight(interpolatedPt, rPt)
            newWt += rPt.Z * wt
            totWt += wt
        newWt /= totWt
        interpolatedPt.Z = newWt
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
        totWt = 0
        newWt = 0
        interpolatedPt = PointValue(x, Y, newWt)
        for rPt in rawPts:
            wt = inverse_weight(interpolatedPt, rPt)
            newWt += rPt.Z * wt
            totWt += wt
        newWt /= totWt
        interpolatedPt.Z = newWt
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
        totWt_p1 = 0
        totWt_p2 = 0
        totWt_p3 = 0
        totWt_p4 = 0

        newWt_p1 = 0
        newWt_p2 = 0            
        newWt_p3 = 0
        newWt_p4 = 0

        interpolatedPt_p1 = PointValue(x, Y, newWt_p1)
        interpolatedPt_p2 = PointValue(x, Y, newWt_p2)
        interpolatedPt_p3 = PointValue(x, Y, newWt_p3)
        interpolatedPt_p4 = PointValue(x, Y, newWt_p4)
        for rPt in rawPts:
            wt_p1 = inverse_weight(interpolatedPt_p1, rPt, p=p1)
            wt_p2 = inverse_weight(interpolatedPt_p2, rPt, p=p2)
            wt_p3 = inverse_weight(interpolatedPt_p3, rPt, p=p3)
            wt_p4 = inverse_weight(interpolatedPt_p4, rPt, p=p4)

            newWt_p1 += rPt.Z * wt_p1
            newWt_p2 += rPt.Z * wt_p2
            newWt_p3 += rPt.Z * wt_p3
            newWt_p4 += rPt.Z * wt_p4
            
            totWt_p1 += wt_p1
            totWt_p2 += wt_p2
            totWt_p3 += wt_p3
            totWt_p4 += wt_p4
        newWt_p1 /= totWt_p1
        newWt_p2 /= totWt_p2
        newWt_p3 /= totWt_p3
        newWt_p4 /= totWt_p4
        
        interpolatedPt_p1.Z = newWt_p1
        interpolatedPt_p2.Z = newWt_p2
        interpolatedPt_p3.Z = newWt_p3
        interpolatedPt_p4.Z = newWt_p4
        
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
 