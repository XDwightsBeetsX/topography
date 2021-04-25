# topography :map:  

Contains different approaches to modeling terrain and maps in python

> Requirements:
>
> - `.csv` file with incomplete sampled terrain

## Inverse Distance Weighting  

A given point `P(x, y)` is determined by the values of its neighbors, inversely to the distance of each neighbor.  

This ensures a `P` is more dependent on nearer points.  

- Weighting function `W(x, y)`
  - Normalized by `ln(x, y)`

## Nearest (Natural) Neighbor  

`P(x, y)` is determined only by the value of its nearest neighbor.  

## Spline  

A 2D-spline is fit to known points, where unknown points `P(x, y)` can be determined.  
