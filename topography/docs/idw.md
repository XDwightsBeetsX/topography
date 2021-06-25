# Inverse Distance Weighting Interpolation

Inverse distance weighting is the interpolation of intermediate points by considering their distance to known points.  
Values at locations nearer to known points are increasingly likely to be similar to the known points, and are weighted based on the inverse of their distance to that point.

All in all, the further away from a point of interest a known point is, the less influence it exerts over determining the interpolated value, like gravity.

In 2d, this is demonstrated mathematically by:

![image](https://user-images.githubusercontent.com/55027279/123363434-20328a00-d538-11eb-98f8-81af053ba7b3.png)

where *u* is an unknown value at some distance *x*, and is calculated from the weights and values of known points *w_i* and *u_i*. These weights are calculated via a static weighting function of the form,

![image](https://user-images.githubusercontent.com/55027279/123363389-02652500-d538-11eb-857e-ab6728ba5b9c.png)

where greater values of *p* assign greater influence to values closest to the interpolated point.

The weight sum with point density *rho* can be then approximated by,

![image](https://user-images.githubusercontent.com/55027279/123364632-6688e880-d53a-11eb-9175-6590cb7ab3bb.png)

which diverges for *p <= 2* as *R* approaches infinity. This means that for weighting function power parameters *p <= 2*, interpolated values become dominated by far-away points. 

## Shepard's Method

Shepard worked to minimize a measure of deviations between tuples of interpolating points (x, u) and interpolated points (x_i, u_i),

![image](https://user-images.githubusercontent.com/55027279/123363344-e3669300-d537-11eb-93f5-d098ac844f1d.png)

The power parameter *p* can be tailored to a data set based on understanding of the distribution of known points.

### An example for *p = 2*,

| Shepard's method| *topography* reproduction |
| :-: | :-: |
| ![image](https://user-images.githubusercontent.com/55027279/123361851-60443d80-d535-11eb-8761-a0017807b56a.png) | ![image](https://user-images.githubusercontent.com/55027279/123362265-05f7ac80-d536-11eb-888d-f3bc74cf73e0.png) |

> *credit to: [ArcGIS IDW](https://pro.arcgis.com/en/pro-app/latest/help/analysis/geostatistical-analyst/how-inverse-distance-weighted-interpolation-works.htm), [Wikipedia](https://en.wikipedia.org/wiki/Inverse_distance_weighting)*
