"""
Contains utility and math methods for use by Map

TODO inverse_weight normalize/smoothen
TODO inverse_weight neightborhood check
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
