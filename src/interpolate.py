



def idw(Map):
    pass


def nearest_neighbor(Map):
    pass


def spline(Map):
    pass


def euclidian_distance(ptA, ptB):
    """
    ptA is known, ptB is unknown
    """
    return ( (ptA.X - ptB.X)**2 + (ptA.Y - ptB.Y)**2 ) ** (1/2)


def inverse_weight2D(ptA, ptB):
    """
    ptA is known, ptB is unknown
    """
    return 1 / euclidian_distance(ptA, ptB)


def inverse_weight1D(xA, xB):
    """
    ptA is known, ptB is unknown
    """
    return 1 / (abs(xA - xB))
