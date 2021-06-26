"""
Noise generation
"""

from .Points import PointValue

import random


class Noise(object):
    """
    Noise generator object. Instantiate it with an x and y range.
    """

    def __init__(self, xRange, yRange):
        """
        Ranges are expected in tuples or lists such as `Noise((lowerX, upperX), (lowerY, upperY))`
        """
        self.XMin = xRange[0]
        self.XMax = xRange[1]
        self.YMin = yRange[0]
        self.YMax = yRange[1]
    
    def getRandom(self, scaleFactor=1, seed=None):
        """
        Generates a list of PointValues with random values in the range [-1, 1]

        Optionally scale the noise by `scaleFactor`
        """
        
        if seed != None:
            random.seed(seed)
        else:
            random.seed()
        
        pts = []
        for y in range(self.YMin, self.YMax):
            for x in range(self.XMin, self.XMax):
                pts.append(PointValue(x, y, random.random() * scaleFactor))
        
        return pts

    def getPerlin(self, scaleFactor=1):
        """
        Generates a list of PointValues determined by Perlin noise in the range [-1, 1]

        Optionally scale the noise by `scaleFactor`
        """
        pass

    def getSimplex(self, scaleFactor=1):
        """
        Generates a 2D array of Simplex noise in the range [-1, 1]

        Optionally scale the noise by `scaleFactor`
        """
        pass
