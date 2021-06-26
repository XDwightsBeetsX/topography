"""
inverse_weight function tests
"""

from topography.Points import Point, PointValue
from topography.interpolate import inverse_weight
from .msgs import running, passed, failed

from matplotlib import pyplot as plt


def test_1_overlapping():
    testName = "test_1_overlapping"
    running(testName)
    correct = False
    
    x = 3
    y = 4
    z = 1
    
    testPt = Point(x, y)
    knownPt = PointValue(x, y, z)

    wtExp = z
    wtTest = inverse_weight(testPt, [knownPt])
    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName, wtTest, wtExp)
    assert correct


def test_2_distant():
    testName = "test_2_distant"
    running(testName)
    correct = False
    
    x = 3
    y = 4
    z = 1
    far = 10E9

    testPt = Point(x, y)
    knownPt = PointValue(x + far, y + far, z)

    print(knownPt.getString())
    
    wtLim = 10E-6
    wtTest = inverse_weight(testPt, [knownPt])
    if wtTest < wtLim:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName, wtTest, wtLim)
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
    wtTestL = inverse_weight(known, [knownL])
    wtTestR = inverse_weight(known, [knownR])

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
    wtTest = inverse_weight(known1, [known2])

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
    wtTest = inverse_weight(known1, [known2])

    if wtTest == wtExp:
        correct = True
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct
