import random
import math
import numpy as np
import matplotlib.pyplot as plt
from KMeans import cluster

class KMeans:

    def __init__(self, dataPoints, k):
        self.k = k
        self.dataPoints = dataPoints
        self.meansIndex = []
        self.hasChanged = False
        #Creates random indexes without replacement, for our initial centroids
        self.meansIndex = [None for c in range(self.k)]
        self.meansIndex = random.sample(range(0,len(self.dataPoints)), self.k)
        self.clusters = [cluster for x in range(self.k)]
        #Creates a new cluster object for each random mean data point
        for i in range(len(self.meansIndex)):
            temporary = self.meansIndex[i]
            temp = cluster.Cluster(self.dataPoints[temporary])
            self.clusters[i] = temp

    #Assigns 
    def cluster(self):

        for i in range(len(self.dataPoints)):
            distance = self.calcDistance(self.dataPoints[i], self.clusters[0].mean)
            minD = distance
            minClusterIndex = 0
            
            for j in range(1, len(self.clusters)):
                distance = self.calcDistance(self.dataPoints[i], self.clusters[j].mean)
                if distance < minD:
                    minD = distance
                    minClusterIndex = j

            tempCluster = self.clusters[minClusterIndex]
            if(len(tempCluster.clusterPoints[0]) == 0):
                tempCluster.clusterPoints[0] = self.dataPoints[i]
            else:
                tempCluster.clusterPoints.append(self.dataPoints[i])
            #self.means[minClusterIndex].addPoint(self.dataPoints[i])
        
    def reCluster(self):
        changed = True
        tempMeans = [[0 for i in range(len(self.clusters[0].mean))] for j in range(self.k)]
        for i in range(len(self.clusters) - 1):
            tempMeans[i] = self.clusters[i].mean
        
        while(changed == True):                  
            for i in self.clusters:
                i.calcCentroid()
                i.clusterPoints = [[]]
            self.cluster()
            changed = False
            for i in range(len(self.clusters) - 1):
                for j in range(len(self.clusters[i].mean) - 1):
                    if (math.fabs(tempMeans[i][j] - self.clusters[i].mean[j])) > 0.00001:
                        changed = True
                tempMeans[i] = self.clusters[i].mean
        #Calculates the distance in between two vectors
    def calcDistance(self, d1, d2):
        distance = 0.0
        for i in range(len(d1) - 1):
            # adds the square of the difference of each variable in the data point
            distance += math.pow((d1[i] - (d2[i])),2) 
        #returns the Euclidean distance between two vectors
        return math.sqrt(distance)
    def graph(self):
        print(self.clusters[0].clusterPoints)
    def print(self):
        for i in self.clusters:
            print(i.clusterPoints)
    def getFitness(self):
        sum = 0
        for cluster in self.clusters:
            sum += cluster.calcFitness()
        return (sum / self.k)
if __name__ == "__main__":
    data = [[1,1],[1,1],[2,2],[2,2],[5,5]]
    means1 = KMeans(data, 2)
    means1.cluster()
    means1.reCluster()
    means1.graph()