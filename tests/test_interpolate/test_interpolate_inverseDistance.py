"""
inverse_weight function tests
"""

from topography.Points import Point, PointValue
from topography.interpolate import inverse_weight
from tests.msgs import running, passed, failed

from matplotlib import pyplot as plt


def test_1_overlapping():
    testName = "test_1_overlapping"
    running(testName)
    correct = False
    
    x = 3
    y = 4
    z = 5
    
    p = Point(x, y)
    pv = PointValue(x, y, z)

    expWt = z
    gotWt = inverse_weight(p, [pv])
    
    correct = gotWt == expWt
    
    if correct: passed(testName)
    else: failed(testName, gotWt, expWt)
    assert correct


def test_2_singleRawPt():
    testName = "test_2_singleRawPt"
    running(testName)
    correct = False
    
    x = 3
    y = 4
    z = 5
    d = 10E3

    p = Point(x, y)
    pv = PointValue(x+d, y+d, z)
    
    expWt = z
    gotWt = inverse_weight(p, [pv])
    
    correct = gotWt == expWt
    
    if correct: passed(testName)
    else: failed(testName, gotWt, expWt)
    assert correct


def test_3_symmetric():
    testName = "test_3_symmetric"
    running(testName)
    correct = False
    
    x = 3
    y = 4
    z = 5
    d = 10

    p1 = Point(x+d, y+d)
    pv = PointValue(x, y, z)
    p2 = Point(x-d, y-d)

    gotWt1 = inverse_weight(p1, [pv])
    gotWt2 = inverse_weight(p2, [pv])

    correct = gotWt1 == gotWt2
    
    if correct: passed(testName)
    else: failed(testName, f"{gotWt1} != {gotWt2}", f"{gotWt1} == {gotWt2}")
    assert correct
