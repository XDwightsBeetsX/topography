"""
Weight Function Testing
"""

from topography.Point import Point
from topography.interpolate import inverse_weight

import numpy as np


def test_1d_easy():
    """
    Tests of weighting in only x
    """
    print("\n[TESTS] - running - test_1d_easy")
    correct = True
    y = 0  # points are in 1D, just use y=0
    v = 0  # constant value ref
    
    known1 = Point(10, y, v)
    known2 = Point(known1.X, y, v)  # d(P1, P2) = 0

    wExpected0 = 1
    wTest0 = inverse_weight(known1, known2, onlyX=True)
    if wTest0 != wExpected0:
        correct = False
    
    known3 = Point(known1.X-1, y, v)  # d(P1, P3) = 1
    wExpected1 = np.exp(-1)
    wTest1 = inverse_weight(known1, known3, onlyX=True)
    if wTest1 != wExpected1:
        correct = False
    
    if correct: print("[TESTS] - passed  - test_1d_easy")
    else: print("[TESTS] - failed  - test_1d_easy")
    assert correct


def test_1d_symmetry():
    """
    Tests weighting in only x about symmetrical point
    """
    print("\n[TESTS] - running - test_1d_symmetry")
    correct = True
    y = 0  # points are in 1D, just use y=0
    v = 0  # constant value ref

    known = Point(5, y, v)
    
    kx = known.X/4
    testSym1 = Point(known.X - kx, y, v)
    testSym2 = Point(known.X + kx, y, v)
    if inverse_weight(known, testSym1, onlyX=True) != inverse_weight(known, testSym2, onlyX=True):
        correct = False
    
    if correct: print("[TESTS] - passed  - test_1d_symmetry")
    else: print("[TESTS] - failed  - test_1d_symmetry")
    assert correct

def test_1d_hard():
    """
    Tests weighting in only x at different distances
    """
    print("\n[TESTS] - running - test_1d_hard")
    correct = True
    y = 0
    v = 0

    # Spaced 1 apart
    k1x, k2x = 4, 5
    known1 = Point(k1x, y, v)
    known2 = Point(k2x, y, v)

    wExpected1 = np.exp(-abs(k1x-k2x))
    wTest1 = inverse_weight(known1, known2, onlyX=True)
    if wTest1 != wExpected1:
        correct = False
    
    # Spaced 3 apart with values 0, 5
    c1x, c2x = 2, 5
    known3 = Point(c1x, y, v)
    known4 = Point(c2x, y, v)
    
    wExpected2 = np.exp(-abs(c1x-c2x))
    wTest2 = inverse_weight(known3, known4, onlyX=True)
    if wTest2 != wExpected2:
        correct = False
    
    if correct: print("[TESTS] - passed  - test_1d_hard")
    else: print("[TESTS] - failed  - test_1d_hard")
    assert correct
