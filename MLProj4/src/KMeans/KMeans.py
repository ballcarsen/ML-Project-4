import random
import math
import numpy as np
import matplotlib.pyplot as plt
from KMeans import cluster

class KMeans:
    dataPoints = [[]]
    means = []
    meansIndex = []
    hasChanged = False
    def __init__(self, dataPoints, k):
        self.k = k
        self.dataPoints = dataPoints
        #Creates random indexes without replacement, for our initial centroids
        self.meansIndex = [None for c in range(self.k)]
        self.meansIndex = random.sample(range(0,len(self.dataPoints)), self.k)
        self.means = [cluster for x in range(self.k)]
        #Creates a new cluster object for each random mean data point
        for i in range(len(self.meansIndex)):
            temporary = self.meansIndex[i]
            temp = cluster.Cluster(self.dataPoints[temporary])
            self.means[i] = temp

    #Assigns 
    def calcMeans(self):

        for i in range(len(self.dataPoints)):
            distance = self.calcDistance(self.dataPoints[i], self.means[0].mean)
            minD = distance
            minClusterIndex = 0
            
            for j in range(1,len(self.means)):
                print(self.dataPoints[i])
                print(self.means[j].mean)
                distance = self.calcDistance(self.dataPoints[i], self.means[j].mean)
                if distance < minD:
                    minD = distance
                    minClusterIndex = j

            tempCluster = self.means[minClusterIndex]
            if(len(tempCluster.clusterPoints[0]) == 0):
                tempCluster.clusterPoints[0] = self.dataPoints[i]
            else:
                tempCluster.clusterPoints.append(self.dataPoints[i])
            #self.means[minClusterIndex].addPoint(self.dataPoints[i])
        
    def reCluster(self):
        changed = True
        tempMeans = [[0 for i in range(len(self.means[0].mean))] for j in range(self.k)]
        for i in range(len(self.means) - 1):
            tempMeans[i] = self.means[i].mean
        
        while(changed == True):                  
            for i in self.means:
                i.calcCentroid()
            self.calcMeans()
            changed = False
            for i in range(len(self.means) - 1):
                for j in range(len(self.means[i].mean) - 1):
                    if (math.fabs(tempMeans[i][j] - self.means[i].mean[j])) > 0.00001:
                        changed = True
                tempMeans[i] = self.means[i].mean
        #Calculates the distance in between two vectors
    def calcDistance(self, d1, d2):
        distance = 0.0
        for i in range(len(d1) - 1):
            # adds the square of the difference of each variable in the data point
            distance += math.pow((d1[i] - (d2[i])),2) 
        #returns the Euclidean distance between two vectors
        return math.sqrt(distance)
    def graph(self):
        print(self.means[0].clusterPoints)
if __name__ == "__main__":
    data = [[1,1],[1,1],[2,2],[2,2],[5,5]]
    means1 = KMeans(data, 2)
    means1.calcMeans()
    means1.reCluster()
    means1.graph()