"""
Example driver program
"""

from topography.Map import Map
from topography.utils.io import getPointValuesFromCsv


if __name__ == "__main__":
    # take in csv/xlsx
    rawData = getPointValuesFromCsv("tests/data/20x20.csv")

    # make map from rawData
    M = Map(rawData)
    # M.showRawPointValues()

    # interpolate
    M.idw(showWhenDone=True)
