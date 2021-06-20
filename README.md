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

## ***Usage***

### ***Install***

```shell
pip install topography
```

### ***Implementation***

```python
from topography.Map import Map
from topography.utils.io import getPointValuesFromCsv

# read in data
rawDataPts = getPointValuesFromCsv("measurements.csv")

# create a Map object
M = Map(rawDataPts)

# perform interpolation
M.idw(showWhenDone=True)

# save to file
M.writeFilledPointValuesToCsv(self, "idw_results", writeAsMatrix=True)
```

## ***Features***

### **Inverse Distance Weighting (IDW)**

A given point `P(x, y)` is determined by the values of its neighbors, inversely to the distance of each neighbor.  

This ensures `P` is more dependent on nearer points.  

- Weighting function `w(x, y)` of the form `exp(-d(x, y))`

### **Nearest Neighbor (NN) *[in progress]***

`P(x, y)` is determined only by the value of its nearest neighbor.

In the case of an exact tie, ***TODO***

### **Spline *[in progress]***

A 2D-spline is fit to known points, where unknown points `P(x, y)` can be determined by their intersection with the fitted surface.

## ***Development with `twine`***

```shell
python setup.py sdist bdist_wheel
twine upload -r pypi dist/* -u <username> -p <password>
```

### Reference

- *credit to [arcGIS](https://www.arcgis.com/index.html)*
  - *[Inverse Distance Weighting (IDW)](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geostatistical-analyst/how-inverse-distance-weighted-interpolation-works.htm)*

  - *[Nearest Neighbor (NN)](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-average-nearest-neighbor-distance-spatial-st.htm)*

  - *[Spline](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/how-spline-works.htm)*
