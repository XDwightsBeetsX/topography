"""
Map idw function tests

NOTE these implement np.exp() to check the weights
so the equation used must be implemented in testing
"""

from topography.Map import Map
from topography.Points import PointValue
from tests.msgs import running, passed, failed

import numpy as np


def getTestMap(w, h, val=0):
    pts = []
    for y in range(h):
        for x in range(w):
            pts.append(PointValue(x, y, val))
    
    return Map(pts)


class TestMap(object):
    def test_ctor(self):
        testName = "TestMapWxH.test_ctor"
        running(testName)
        correct = True
        
        H = 5
        W = 3
        M = getTestMap(W, H)
        correct = len(M.RawPointValues) == H*W
        
        gotXr = M.XRange
        expXr = (0, W-1)
        correct = gotXr == expXr
        if not correct: failed(testName, gotXr, expXr)

        gotYr = M.YRange
        expYr =  (0, H-1)
        correct = gotYr == expYr
        if not correct: failed(testName, gotYr, expYr)

        if correct: passed(testName)
        assert correct
    
    def test_addPointValue(self):
        testName = "TestMapWxH.test_addPointValue"
        running(testName)
        correct = True

        H = 3
        W = 4
        M = getTestMap(W, H)

        M.addRawPointValue(PointValue(W+1, H+1, 0))
        gotL = len(M.RawPointValues)
        expL = H*W + 1
        correct = gotL == expL
        if not correct: failed(testName, gotL, expL)

        if correct: passed(testName)
        assert correct

    def test_removeRawPointValue(self):
        testName = "TestMapWxH.test_removeRawPointValue"
        running(testName)
        correct = True

        H = 6
        W = 6
        M = getTestMap(W, H)

        gotL = len(M.RawPointValues)
        expL = H*W
        correct = gotL == expL
        if not correct: failed(testName, gotL, expL)

        M.removeRawPointValue(W-1, H-1)
        
        gotL = len(M.RawPointValues)
        expL = H*W - 1
        correct = gotL == expL
        if not correct: failed(testName, gotL, expL)

        if correct: passed(testName)
        assert correct
