"""
Example driver program
"""

from topography.Map import Map
from topography.io import getPointsFromCsv


if __name__ == "__main__":
    # take in csv/xlsx
    rawData = getPointsFromCsv("tests/test_data/test_2d_basic.csv")

    # make map from rawData
    M = Map(rawData)
    M.showRawPointValues()

    # interpolate
    M.idw(showWhenDone=True)

    # check out data after interpolating
    M.showFilledPointValues()
