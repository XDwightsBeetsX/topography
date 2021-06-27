"""
interpolate.euclidian_distance tests
"""

from topography.Points import Point
from topography.utils.pile import euclidian_distance
from tests.msgs import running, passed, failed


def test_1_overlapping():
    testName = "test_1_overlapping"
    running(testName)
    correct = False
    
    known1 = Point(0, 0)
    known2 = Point(0, 0)

    dExp = 0
    dTest = euclidian_distance(known1, known2)

    correct = dExp == dTest

    if correct: passed(testName)
    else: failed(testName, dTest, dExp)
    assert correct


def test_2_unitDistance():
    testName = "test_2_unitDistance"
    running(testName)
    correct = False

    d = 1
    known1 = Point(0, 0)
    known2 = Point(0 + d, 0)

    dExp = d
    dTest = euclidian_distance(known1, known2)

    correct = dExp == dTest
    
    if correct: passed(testName)
    else: failed(testName, dTest, dExp)
    assert correct


def test_3_pythag():
    testName = "test_3_pythag"
    running(testName)
    correct = False
    
    d = 10
    known1 = Point(0, 0)
    known2 = Point(6, 8)

    dExp = d
    dTest = euclidian_distance(known1, known2)

    correct = dExp == dTest

    if correct: passed(testName)
    else: failed(testName, dTest, dExp)
    assert correct
