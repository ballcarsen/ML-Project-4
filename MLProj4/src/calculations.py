import math
from matplotlib import pyplot as plt
import numpy as np

def calcDistance(d1, d2):
    distance = 0.0
    for i in range(len(d1)):
        # adds the square of the difference of each variable in the data point
        #print(d1[i])
        #print(d2[i])
        distance += math.pow((d1[i] - (d2[i])), 2)
        # returns the Euclidean distance between two vectors
    return math.sqrt(distance)

def graph(data, k):
    colors = ['yellow', 'gray', 'pink', 'orange', 'black', 'blue','red','green','purple']
    for i in range(k):
        if len(data[i]) > 1:
            #print(data[i] , 'data')
            x,y = np.array(data[i]).T
            plt.scatter(x,y, c = colors[i])
    plt.show()

# calculates the average silhouette coefficient for all points in the dataset
def avgSilhouetteFitness(clusters, data):
    totalSum = 0
    for cluster in clusters:
        clusterSilhouetteValSum = 0
        for point in cluster:
            leastAvgDistToOther = findLeastAvgDistToOther(point, cluster, clusters)
            AvgDistWithin = findAvgDistWithin(point, cluster)
            silhouetteVal = getSilhouette(leastAvgDistToOther,AvgDistWithin)
            clusterSilhouetteValSum += silhouetteVal
        if(len(cluster) != 0):
            clusterSilhouetteValAvg = clusterSilhouetteValSum / len(cluster)
            totalSum += clusterSilhouetteValAvg
    return totalSum / len(clusters)


def getSilhouette(b,a):
    coefficient = None
    if (a < b):
        coefficient = 1 - (a/b)
    elif(a > b):
        coefficient = (b/a) - 1
    else:
        coefficient = 0
    return coefficient



def findAvgDistWithin(point, cluster):
    sumDist = 0
    for otherPoint in cluster:
        sumDist += calcDistance(point,otherPoint)
    return sumDist / len(cluster)

def findLeastAvgDistToOther(point, cluster, clusters):
    leastAvgDistance = math.inf

    for otherCluster in clusters:
        sumDistance = 0
        if (not equalLists(cluster, otherCluster)):

            for otherPoint in otherCluster:
                sumDistance += calcDistance(point,otherPoint)
            if (len(otherCluster) != 0):
                avgDistance = sumDistance / len(otherCluster)
                if (avgDistance < leastAvgDistance):
                    leastAvgDistance = avgDistance

    return leastAvgDistance

def equalLists(list1, list2):
    if(len(list2) == 0):
        return False
    for i in range(len(list1[0])):
        if (list1[0][i] != list2[0][i]):
            return False
    return True
