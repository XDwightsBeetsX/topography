# ***topography :earth_americas:***

![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
[![Build Status](https://travis-ci.com/XDwightsBeetsX/topography.svg?branch=master)](https://travis-ci.com/XDwightsBeetsX/topography)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/XDwightsBeetsX/topography.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/XDwightsBeetsX/topography/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/XDwightsBeetsX/topography.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/XDwightsBeetsX/topography/alerts/)

Contains different approaches to modeling terrain and topographic-style maps in python

![image](https://user-images.githubusercontent.com/55027279/123488764-2b3bf780-d5d6-11eb-9c7e-3e9cd3020018.png)

## ***Features***

### **[Inverse Distance Weighting (IDW)](/topography/docs/idw.md)**

A given point `P(x, y)` is determined by the values of its neighbors, inversely to the distance of each neighbor.  

`P` is more heavily influenced by nearer points via a weighting function `w(x, y)`.

### **Steps**

The value of `P(x, y)` is determined only by the closest raw data point.

This approach works best to get a "feel" for larger datasets. With few input points, the resulting map has little detail.

In the case of multiple equidistant points being closest, point values are stored, and averaged.

### **Nearest Neighbor (NN)**

*in progress :construction_worker: :hammer_and_wrench:*

## ***Install***

```shell
pip install topography
```
### ***Requirements***

- `numpy`
- `matplotlib`

*see the [requirements.txt](requirements.txt)*

### ***Example***

```python
from topography.Map import Map
from topography.utils.io import getPointValuesFromCsv

# make map from recorded data
rawData = getPointValuesFromCsv("tests/data/20x20.csv")
M = Map(rawData)

# make map from noise data
# noiseMaker = Noise((0, 50), (0, 50))
# noiseData = noiseMaker.getRandom(scaleFactor=1)
# M = Map(noiseData)

# Display the inputted raw data values
# M.showRawPointValues()

# interpolate using inverse distance weighting
M.idw(showWhenDone=True)

# Display the interpolated data values
# M.showFilledPointValues()

# Save the data to a .csv file
# optionally, write to file as a matrix, the default is x, y, z columns
M.writeLastToCsv("idw_20x20", writeAsMatrix=True)
```
