"""
Plotting of Map data
"""

from matplotlib import pyplot as plt


def heatmap(matrix):
    plt.imshow(matrix)
    plt.colorbar()
    plt.show()
