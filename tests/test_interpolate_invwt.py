"""
idw function tests

NOTE these implement np.exp() to check the weights
so the equation used must be implemented in testing
"""

from topography.Points import Point, PointValue
from topography.interpolate import inverse_weight
from .msgs import running, passed, failed

from matplotlib import pyplot as plt


# points in 2D just use y=0
Y = 0

def test_1_overlapping():
    testName = "test_1_overlapping"
    running(testName)
    correct = False
    
    known1 = Point(0, 0)
    known2 = Point(0, 0)

    wtExp = 1
    wtTest = inverse_weight(known1, known2)
    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct

def test_2_unitDistance():
    testName = "test_2_unitDistance"
    running(testName)
    correct = False
    
    known1 = Point(0, 0)
    known2 = Point(0, 1)

    wtExp = 1
    wtTest = inverse_weight(known1, known2)
    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct

def test_3_symmetric():
    testName = "test_3_symmetric"
    running(testName)
    correct = False
    
    d = 3
    knownL = Point(0 - d, 0)
    known = Point(0, 0)
    knownR = Point(0 + d, 0)

    wtExp = 1 / (d**2)
    wtTestL = inverse_weight(known, knownL)
    wtTestR = inverse_weight(known, knownR)

    if wtTestL == wtExp and wtTestR == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct

def test_4_far():
    testName = "test_4_far"
    running(testName)
    correct = False
    
    d = 10E5
    known1 = Point(0, 0)
    known2 = Point(0 + d, 0)

    wtExp = 1 / (d**2)
    wtTest = inverse_weight(known1, known2)

    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct

def test_5_2d():
    testName = "test_5_2d"
    running(testName)
    correct = False
    
    known1 = Point(0, 0)
    known2 = Point(3, 4)

    wtExp = 1 / (5**2)
    wtTest = inverse_weight(known1, known2)

    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct
