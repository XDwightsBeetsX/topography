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

    # Display the inputted raw data values
    # M.showRawPointValues()

    # interpolate using inverse distance weighting
    M.idw(showWhenDone=True)

    # Display the interpolated data values
    # M.showFilledPointValues()

    # Save the data to a .csv file
    # M.writeLastToCsv("idw_20x20", writeAsMatrix=True)
