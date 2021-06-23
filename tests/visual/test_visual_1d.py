"""
interpolate.euclidian_distance tests
"""

from topography.Points import PointValue
from topography.interpolate import inverse_weight, euclidian_distance
from ..msgs import running, passed, failed

import numpy as np
from matplotlib import pyplot as plt


def test_1d_p2():
    Y = 0
    n = 50
    newXs = np.linspace(0, 5, n)

    rawPts = []
    rawPts.append(PointValue(1, Y, 2))
    rawPts.append(PointValue(2, Y, 4))
    rawPts.append(PointValue(3, Y, 4))
    rawPts.append(PointValue(4, Y, 2))

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
    
    plotXs = [pt.X for pt in totPts]
    plotZs = [pt.Z for pt in totPts]
    plt.plot(plotXs, plotZs)
    plt.show()


def test_1d_comparison():
    """
    Comparisons of power P across a set of points from Shepard's method
    """
    p1 = 1
    p2 = 2
    p3 = 3
    p4 = 5

    Y = 0
    n = 50
    newXs = np.linspace(0, 5, n)

    rawPts = []
    rawPts.append(PointValue(1, Y, 2))
    rawPts.append(PointValue(2, Y, 4))
    rawPts.append(PointValue(3, Y, 4))
    rawPts.append(PointValue(4, Y, 2))

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
    
    fig, ax = plt.subplots(4, sharex='col', squeeze=True)
    fig.suptitle("Comparisons of power P across a set of points from Shepard's method")
    ax[0].plot(newXs, [pt.Z for pt in pts_p1])
    ax[1].plot(newXs, [pt.Z for pt in pts_p2])
    ax[2].plot(newXs, [pt.Z for pt in pts_p3])
    ax[3].plot(newXs, [pt.Z for pt in pts_p4])

    ax[0].set_ylim(0, 5)
    ax[1].set_ylim(0, 5)
    ax[2].set_ylim(0, 5)
    ax[3].set_ylim(0, 5)
    
    ax[0].set_title(f"P = {p1}")
    ax[1].set_title(f"P = {p2}")
    ax[2].set_title(f"P = {p3}")
    ax[3].set_title(f"P = {p4}")
    
    plt.show()
 