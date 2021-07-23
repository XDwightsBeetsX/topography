"""
Various helper methods for topography
"""

from ..Points import Point, PointValue


def euclidian_distance(ptA, ptB):
    """
    Returns the shortest path distance between two Points or PointValues
    """
    if isinstance(ptA, PointValue) and isinstance(ptB, PointValue):
        return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 + (ptA.Z - ptB.Z)**2 ) ** (1/2)
    elif isinstance(ptA, Point) and isinstance(ptB, Point):
        return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)
    else:
        raise Exception(f"invalid point types: {type(ptA)}, {type(ptB)}")
