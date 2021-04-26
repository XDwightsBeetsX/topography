
import numpy as np


def idw(Map):
    pass


def nearest_neighbor(Map):
    pass


def spline(Map):
    pass


def euclidian_distance(ptA, ptB):
    """
    ptA is known, ptB is unknown  
        returns: 2D linear shortest path distance 
    """
    return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)


def inverse_weight(ptA, ptB, modifier=1.0, onlyX=False):
    """
    ptA is known, ptB is unknown  
    greater modifier -> nearer points have larger impact  
    onlyX typically used for testing  
        returns: weighting on [0, 1] to a nearby point value (ptB)
    """
    if onlyX:
        return np.exp(-modifier*abs(ptA.X - ptB.X))
    else:
        return np.exp(-modifier*euclidian_distance(ptA, ptB))
