"""
Weight Function Testing
"""

from src.Point import Point
from src.interpolate import inverse_weight

import numpy as np


def test_1d_singlePt():
    """
    Tests of weighting in only x
    """
    correct = True
    y = 0  # points are in 1D, just use y=0
    m = 1  # exponent modifier
    v = .8  # constant value ref
    known = Point(10, y, 1)

    # Check weighting function against function and constant
    # d(P1, P2) = 0
    testF0 = Point(known.X, y, v)
    # verifty function
    wFunction0 = np.exp(-m*abs(known.X - testF0.X))
    # verify expected value
    wExpected0 = 1
    wTest0 = inverse_weight(known, testF0, onlyX=True)
    if wTest0 != wFunction0 or wTest0 != wExpected0:
        correct = False
    
    # Check weighting function against function and constant
    # d(P1, P2) = 1
    testF1 = Point(known.X-1, y, v)
    # verifty function
    wFunction1 = np.exp(-m*abs(known.X - testF1.X))
    # verify expected value
    wExpected1 = np.exp(-1)
    wTest1 = inverse_weight(known, testF1, onlyX=True)
    if wTest1 != wFunction1 or wTest1 != wExpected1:
        correct = False
    
    # Symmetry about known
    vS = known.Value - known.Value/2
    kx = known.X/4
    testSym1 = Point(known.X - kx, y, vS)
    testSym2 = Point(known.X + kx, y, vS)
    if inverse_weight(known, testSym1, onlyX=True) != inverse_weight(known, testSym2, onlyX=True):
        correct = False
    
    assert correct


def test_1d_multiPt():
    """
    Tests of weighting in only x but with multiple points
    """
    correct = True

    assert correct
