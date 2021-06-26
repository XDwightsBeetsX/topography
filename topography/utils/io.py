"""
Data I/O such as reading from file
"""

from topography.Points import PointValue


def getPointValuesFromCsv(filename):
    """
    Reads pointValues in from csv in the form:  
        x, y, z(value)
    """
    try:
        with open(filename, 'r+') as f:
            pointValues = []
            # skip first line of headers "x, y, z\n"
            for line in f.readlines()[1:]:
                l = line.split(',')

                x = int(l[0])
                y = int(l[1])
                z = float(l[2])
                
                p = PointValue(x, y, z)
                pointValues.append(p)
            return pointValues
    except Exception:
        print(f"[MAP]-[readFromCsv]-[ERROR]-could not read pointValues from file '{filename}'")


def generateRandomPointValues(xRange, yRange):
    pass
