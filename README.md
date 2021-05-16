# topography :earth_americas:  

![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
[![Build Status](https://travis-ci.com/XDwightsBeetsX/topography.svg?branch=master)](https://travis-ci.com/XDwightsBeetsX/topography)

Contains different approaches to modeling terrain and maps in python

Requirements:  

- `.csv` file with incomplete sampled terrain

## [Inverse Distance Weighting](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geostatistical-analyst/how-inverse-distance-weighted-interpolation-works.htm)  

A given point `P(x, y)` is determined by the values of its neighbors, inversely to the distance of each neighbor.  

This ensures a `P` is more dependent on nearer points.  

- Weighting function `W(x, y)`
  - Normalized by `exp(-d(x, y))`

## [Nearest (Natural) Neighbor](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/h-how-average-nearest-neighbor-distance-spatial-st.htm)  

`P(x, y)` is determined only by the value of its nearest neighbor.  

## [Spline](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/how-spline-works.htm)  

A 2D-spline is fit to known points, where unknown points `P(x, y)` can be determined.  

> *References made to [`arcGIS`](https://www.arcgis.com/index.html)*
