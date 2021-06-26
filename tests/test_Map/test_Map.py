"""
Map idw function tests

NOTE these implement np.exp() to check the weights
so the equation used must be implemented in testing
"""

from topography.Map import Map
from topography.utils.io import getPointValuesFromCsv
from .msgs import running, passed, failed

import numpy as np


def test_1_basic():
    testName = "test_1_basic"
    running(testName)
    correct = True
    
    testData = getPointValuesFromCsv("tests/data/2x2.csv")
    M = Map(testData)
    M.idw(showWhenDone=False)
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct


def test_2_big():
    testName = "test_2_big"
    running(testName)
    correct = True
    
    testData = getPointValuesFromCsv("tests/data/100x100.csv")
    M = Map(testData)
    M.idw(showWhenDone=False)
    
    if correct: passed(testName)
    else: failed(testName)
    assert correct
