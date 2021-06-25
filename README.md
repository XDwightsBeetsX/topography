# ***topography :earth_americas:***

![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
[![Build Status](https://travis-ci.com/XDwightsBeetsX/topography.svg?branch=master)](https://travis-ci.com/XDwightsBeetsX/topography)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/XDwightsBeetsX/topography.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/XDwightsBeetsX/topography/context:python)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/XDwightsBeetsX/topography.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/XDwightsBeetsX/topography/alerts/)

Contains different approaches to modeling terrain and topographic-style maps in python

## ***Requirements***

- `numpy`
- `matplotlib`

*see the [requirements.txt](requirements.txt)*

## ***Install***

```shell
pip install topography
```

## ***Features***

### **[Inverse Distance Weighting (IDW)](/topography/docs/idw.md)**

A given point `P(x, y)` is determined by the values of its neighbors, inversely to the distance of each neighbor.  

`P` is more heavily influenced by nearer points via a weighting function `w(x, y)`.

### **Nearest Neighbor (NN) *[in progress :construction_worker: :hammer_and_wrench:]***

`P(x, y)` is determined only by the value of its nearest neighbor.

This approach works better with a larger set of data points, or else the resulting map has little detail.

In the case of an exact tie, ***TODO***

### **Spline *[in progress :construction_worker: :hammer_and_wrench:]***

## ***Example***

```python
from topography.Map import Map
from topography.utils.io import getPointValuesFromCsv

# take in csv/xlsx
rawData = getPointValuesFromCsv("tests/data/20x20.csv")

# make map from rawData
M = Map(rawData)

# Display the inputted raw data values
M.showRawPointValues()

# interpolate using inverse distance weighting
M.idw(showWhenDone=True)

# Display the interpolated data values
M.showFilledPointValues()

# Save the data to a .csv file
M.writeLastToCsv("idw_20x20", writeAsMatrix=True)
```

### ***Development with `twine`***

```shell
python setup.py sdist bdist_wheel
twine upload -r pypi dist/* -u <username> -p <password>
```

> *credit to: [ArcGIS](https://www.arcgis.com/index.html)*
