"""
Contains utility and math methods for use by Map

TODO inverse_weight normalize/smoothen
TODO inverse_weight neightborhood check
"""

import numpy as np


def euclidian_distance(ptA, ptB):
    """
    Returns the shortest path distance between the two points
    """
    return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)


def inverse_weight(ptA, ptB, onlyX=False):
    """
    ptA is known, ptB is unknown  
    greater modifier -> nearer points have larger impact  
    onlyX typically used for testing  
        returns: weighting on [0, 1] to a nearby point value ptB
    """
    if onlyX:
        return np.exp(-abs(ptA.X - ptB.X))
    else:
        return np.exp(-euclidian_distance(ptA, ptB))
