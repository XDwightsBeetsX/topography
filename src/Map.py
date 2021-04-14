

from .interpolate import *


class Map(object):
    def __init__(self, contents):
        """
        map is 2D array or vector-like of Points
        """
        self.Contents = contents
        self.xLen = len(contents[0])
        self.yLen = len(contents)
        self.MinVal, self.MaxVal = self.getMinMax()
    
    def getMinMax(self):
        v0 = self.Contents[0][0].Value
        currMax = v0
        currMin = v0
        for i in range(self.xLen):
            for j in range(self.yLen):
                v = self.Contents[i][j].Value
                if currMax < v:
                    currMax = v
                elif v < currMin:
                    currMin = v
        
        return currMin, currMax

    def show(self):
        print(self.Contents)
