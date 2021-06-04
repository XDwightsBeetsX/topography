
from topography.Map import Map, getDataFromCsv

if __name__ == "__main__":
    # take in csv/xlsx
    data = getDataFromCsv("test.csv")

    # malke map
    M = Map(data)
    M.show()

    # interpolate
    M.idw()
