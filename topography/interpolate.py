"""
Contains utility and math methods for use by Map
"""

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
        for keyVal in distsAndVals[distKey]:
            if neighborhoodSize is not None:
                if neighborhoodSize <= ct:
                    return totVal / totWt
            wt = 1
            if distKey != 0:
                wt = 1 / (distKey**p)
            totVal += wt * keyVal
            totWt += wt
            ct += 1
    
    return totVal / totWt

def step(thisPt, rawPts, limit):
    """
    returns the nearest step value.  
    In the case of several equidistant `rawPts`, returns an average of the nearest values
    """
    stepVals = []
    currMin = limit
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
