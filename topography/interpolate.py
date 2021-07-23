"""
Contains utility and math methods for use by Map
"""

from typing import NewType
from .utils.pile import euclidian_distance


def inverse_weight(thisPt, rawPts, p=2, neighborhoodSize=None):
    """
    `thisPt` - unknown PointValue

    `rawPts` - the set of known PointValues

    `p` - (power) is set to 2 by default

    `neighborhoodSize` - integer number of nearest points to consider

    returns the weight between two points. If a neighborhood is specified, only considers a number of the closest points
    """
    distsAndVals = {}
    for pt in rawPts:
        d = euclidian_distance(thisPt, pt)
        if d in distsAndVals.keys():
            distsAndVals[d].append(pt.Z)
        else:
            distsAndVals[d] = [pt.Z]
        
    # Check to see if only considering nearest neighborhoodSize points
    distKeys = distsAndVals.keys()
    if neighborhoodSize is not None:
        distKeys = sorted(distKeys)
    
    totVal = 0
    totWt = 0
    ct = 0
    for distKey in distKeys:
        for val in distsAndVals[distKey]:
            if neighborhoodSize is not None:
                if neighborhoodSize <= ct:
                    return totVal / totWt
            wt = 1
            if distKey != 0:
                wt = 1 / (distKey**p)
            totVal += wt * val
            totWt += wt
            ct += 1
    
    return totVal / totWt


def step(thisPt, rawPts):
    """
    `thisPt` - unknown PointValue

    `rawPts` - the set of known PointValues  

    returns the nearest step value.

    In the case of several equidistant `rawPts`, returns an average of the nearest values
    """
    stepVals = []
    currMin = rawPts[0].Z
    for pt in rawPts:
        d = euclidian_distance(thisPt, pt)
        if d == currMin:
            stepVals.append(pt.Z)
        elif d < currMin:
            stepVals.clear()
            currMin = d
            stepVals.append(pt.Z)
    
    # if tie, return average of closest values
    if len(stepVals) == 1:
        return stepVals[0]
    return sum(stepVals) / len(stepVals)


def bilinear(thisPt, rawPts):
    """
    `thisPt` - unknown PointValue

    `rawPts` - the set of known PointValues  

    returns the interpolated Z value.

    if fewer than 4 data points have been provided, returns the average
    """
    # check if valid number of raw data points
    l = len(rawPts)
    if l < 4:
        s = 0
        for pt in rawPts:
            s += pt.Z
        return s / l
    
    # find nearest 4 points
    nearest = []  # (pt, dist) pairs
    currMax = 10E10
    for pt in rawPts:
        dist = euclidian_distance(thisPt, pt)
        if dist < currMax:
            if len(nearest) == 4:
                # remove previous furthest
                prevFurthest = nearest[0]
                for ptDist in nearest:
                    if prevFurthest[1] < ptDist[1]:
                        prevFurthest = ptDist
                nearest.pop(prevFurthest)
            
            # update shortest points
            nearest.append((pt, dist))
    
    # perform the bilinear interpolation for thisPt
    ptAA = nearest[0][0]
    ptAB = nearest[1][0]
    ptBA = nearest[2][0]
    ptBB = nearest[3][0]

    zAB = ( (ptAB.Z - ptAA.Z) / (ptAB.X - ptAA.X) ) * (thisPt.X - ptAA.X) + ptAA.Z
    zBA = ( (ptBA.Z - ptBB.Z) / (ptBA.X - ptBB.X) ) * (thisPt.X - ptBB.X) + ptBB.Z

    zZ = ( (zBA - zAB) / (ptAB - ptBB.X) ) * (thisPt.X - ptBB.X) + ptBB.Z
