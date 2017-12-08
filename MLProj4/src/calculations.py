import math
from matplotlib import pyplot as plt
import numpy as np
def calcDistance(d1, d2):
    distance = 0.0
    for i in range(len(d1)):
        # adds the square of the difference of each variable in the data point
        distance += math.pow((d1[i] - (d2[i])), 2)
        # returns the Euclidean distance between two vectors
    return math.sqrt(distance)

def graph(data, k):
    colors = ['yellow', 'gray', 'pink', 'orange', 'black']
    for i in range(k):
        if len(data[i]) > 1:
            print(data[i] , 'data')
            x,y = np.array(data[i]).T
            plt.scatter(x,y, c = colors[i])
    plt.show()
