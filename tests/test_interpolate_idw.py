"""
idw function tests

NOTE these implement np.exp() to check the weights
so the equation used must be implemented in testing
"""

from topography.Points import Point, PointValue
from topography.interpolate import inverse_weight
from .msgs import running, passed, failed

import numpy as np
from matplotlib import pyplot as plt


def w(x, xi, p):
    return 1/abs(x - xi)**p


class Test_Interpolate_Idw:
    # points in 2D just use y=0
    Y = 0

    def test(self):
        xs = [1, 2, 3, 4]
        zs = [2, 4, 4, 2]
        rawPts = []
        rawPts.append(PointValue(xs[0], self.Y, zs[0]))
        rawPts.append(PointValue(xs[1], self.Y, zs[1]))
        rawPts.append(PointValue(xs[2], self.Y, zs[2]))
        rawPts.append(PointValue(xs[3], self.Y, zs[3]))

        newXs = np.linspace(0, 5, 50)
        newPts = []
        for x in newXs:
            if x not in xs:
                p = 2
                val = 0
                totD = 0
                for rPt in rawPts:
                    wt = w(x, rPt.X, p)
                    val += rPt.Z * wt
                    totD += wt
                newPts.append(PointValue(x, self.Y, val/totD))
        
        newZs = [pt.Z for pt in newPts]
        plt.plot(newXs, newZs)
        plt.show()


class Test_Interpolate_Idw_Calculation:
    # points in 2D just use y=0
    Y = 0

    def test_1_overlapping(self):
        testName = "test_1_overlapping"
        running(testName)
        correct = False
        
        X = 10
        known1 = Point(X, self.Y)
        known2 = Point(X, self.Y)

        wExp = 1
        wTest = inverse_weight(known1, known2, onlyX=True)
        if wTest == wExp:
            correct = True
        
        if correct: passed(testName)
        else: failed(testName)
        assert correct

    def test_2_unitDistance(self):
        testName = "test_2_unitDistance"
        running(testName)
        correct = False
        
        X = 10
        known1 = Point(X, self.Y)
        known2 = Point(X + 1, self.Y)

        wExp = np.exp(-1)
        wTest = inverse_weight(known1, known2, onlyX=True)
        if wTest == wExp:
            correct = True
        
        if correct: passed(testName)
        else: failed(testName)
        assert correct

    def test_3_symmetric(self):
        testName = "test_3_symmetric"
        running(testName)
        correct = False
        
        X = 10
        d = 3
        known = Point(X, self.Y)
        knownL = Point(X - d, self.Y)
        knownR = Point(X + d, self.Y)

        wExp = np.exp(-d)
        wTestL = inverse_weight(known, knownL, onlyX=True)
        wTestR = inverse_weight(known, knownR, onlyX=True)

        if wTestL == wExp and wTestR == wExp:
            correct = True
        
        if correct: passed(testName)
        else: failed(testName)
        assert correct

    def test_4_far(self):
        testName = "test_4_far"
        running(testName)
        correct = False
        
        X = 10
        d = 10E5
        known1 = Point(X, self.Y)
        known2 = Point(X + d, self.Y)

        wExp = np.exp(-d)
        wTest = inverse_weight(known1, known2, onlyX=True)

        if wTest == wExp:
            correct = True
        
        if correct: passed(testName)
        else: failed(testName)
        assert correct

    def test_5_2d(self):
        testName = "test_5_2d"
        running(testName)
        correct = False
        
        x = 3
        y = 4
        d = 5
        known1 = Point(0, 0)
        known2 = Point(x, y)

        wExp = np.exp(-d)
        wTest = inverse_weight(known1, known2)

        if wTest == wExp:
            correct = True
        
        if correct: passed(testName)
        else: failed(testName)
        assert correct
