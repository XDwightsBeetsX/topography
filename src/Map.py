

from .interpolate import *
from .Point import Point


class Map(object):
    """
    Stores points in matrix form  

        - Read points from csv  
        - Print points to csv  
        - Output map image
    """
    def __init__(self, contents=[[]]):
        """
        map is 2D array or vector-like of Points
        """
        self.Contents = contents
    
    def readFromCsv(self, filename):
        """
        Reads points in from csv in the form:  
            x,y,value
        """
        # read in csv
        try:
            with open(filename, 'r+') as f:
                points = []
                minX, maxX = 0, 0
                minY, maxY = 0, 0
                for line in f.readlines():
                    l = line.split(',')
                    x = int(l[0])
                    y = int(l[1])
                    val = float(l[2])
                    if x > maxX: maxX = x
                    if minX > x: minX = x
                    if y > maxY: maxY = y
                    if minY > y: minY = y
                    p = Point(x, y, val)
                    points.append(p)
        except Exception:
            print(f"[MAP]-[readFromCsv]-[ERROR]-could not read points from file '{filename}'")
        
        # Set self.Contents
        for j in range(maxY):   # row by row
            for p in points:
                if p.Y == j:    # find points on this row
                    for i in range(maxX):   # add points to row, or fill with None-Points
                        if p.X == i:
                            self.Contents[j][i] = p
                            print(f"added point: {p.getString()}")
                        else:
                            self.Contents[j][i] = Point(i, j, None)
                




    def addPoint(self, newPt):
        """
        Will override if a point has been set at the new point's location
        """
        self.Contents[newPt.Y][newPt.X] = newPt

    def getPointsWithData(self):
        """
        Get points that have been set before analysis
        TODO use these for MinMax
        """
        pass

    # def getMinMax(self):
    #     v0 = self.Contents[0][0].Value
    #     currMax = v0
    #     currMin = v0
    #     for i in range(self.xLen):
    #         for j in range(self.yLen):
    #             v = self.Contents[i][j].Value
    #             if currMax < v:
    #                 currMax = v
    #             elif v < currMin:
    #                 currMin = v
        
    #     return currMin, currMax
    
    def show(self):
        print(self.Contents)
