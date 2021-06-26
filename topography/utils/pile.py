"""
Various helper methods for topography
"""


def euclidian_distance(ptA, ptB):
    """
    Returns the shortest path distance between the two Points
    """
    if (ptA.X != ptB.X or ptA.Y != ptB.Y):
        return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)
    return 0.0
