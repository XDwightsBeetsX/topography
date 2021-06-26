"""
Contains utility and math methods for use by Map
"""


def euclidian_distance(ptA, ptB):
    """
    Returns the shortest path distance between the two points
    """
    if (ptA.X == ptB.X and ptA.Y == ptB.Y):
        return 0.0
    return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)


def inverse_weight(ptA, ptB, p=2):
    """
    Uses Shepard's approach to inverse distance weighting

    p (power) is typically set to 2

    returns the weight between two points
    """
    d = euclidian_distance(ptA, ptB)
    if d == 0:
        return 1.0
    else:
        return 1 / (d**p)


def nearest_neighbor(thisPt, rawPts, limit):
    """
    returns the nearest neighbor value.  
    In the case of several equidistant `rawPts`, returns an average of the nearest values
    """
    nnVals = []
    currMin = limit
    for pt in rawPts:
        d = euclidian_distance(thisPt, pt)
        if d == currMin:
            nnVals.append(pt.Z)
        elif d < currMin:
            nnVals.clear()
            currMin = d
            nnVals.append(pt.Z)
    
    # if tie, return average of closest values
    if len(nnVals) == 1:
        return nnVals[0]
    return sum(nnVals) / len(nnVals)
