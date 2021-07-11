"""
Example driver program
"""

from topography.Map import Map
# from topography.Noise import Noise

from topography.utils.io import getPointValuesFromCsv


if __name__ == "__main__":
    # # make map from noise data
    # noiseMaker = Noise((0, 50), (0, 50))
    # noiseData = noiseMaker.getRandom(scaleFactor=1)
    # M = Map(noiseData)

    # make map from recorded data
    rawData = getPointValuesFromCsv("tests/data/20x20.csv")
    M = Map(rawData)
    
    # # Display the inputted raw data values
    # M.showRawPointValues()

    # # interpolate using inverse distance weighting
    # M.idw(showWhenDone=True)
    M.idw(showWhenDone=True)
    
    # # Display the interpolated data values
    # M.showFilledPointValues()

    # # Save the data to a .csv file
    # # optionally, write to file as a matrix
    # # default is x, y, z
    # M.writeLastToCsv("idw_20x20", writeAsMatrix=True)
