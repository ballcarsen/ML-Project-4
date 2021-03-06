#Imports
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from KMeans import cluster
import calculations as calc

#Kmeans clustering
class KMeans:
    def __init__(self, dataPoints, k):
        self.k = k
        self.dataPoints = dataPoints
        self.meansIndex = []
        self.hasChanged = False
        # Creates random indexes without replacement, for our initial centroids
        self.meansIndex = [None for c in range(self.k)]
        self.meansIndex = random.sample(range(0, len(self.dataPoints)), self.k)
        self.clusters = [cluster for x in range(self.k)]
        # Creates a new cluster object for each random mean data point
        for i in range(len(self.meansIndex)):
            temporary = self.meansIndex[i]
            temp = cluster.Cluster(self.dataPoints[temporary])
            self.clusters[i] = temp

    def setClusters(self, clusters):
        self.clusters = clusters


    # Assigns each data point to the closest center
    def cluster(self):
        #for all data points
        for i in range(len(self.dataPoints)):
            distance = self.calcDistance(self.dataPoints[i], self.clusters[0].mean)
            #Minimum distance from the point to a center
            minD = distance
            #Corresponding cluster index closest to the point i
            minClusterIndex = 0
            #Calcualtes the distance from the point i, to all the cluster centers
            for j in range(1, len(self.clusters)):
                distance = self.calcDistance(self.dataPoints[i], self.clusters[j].mean)
                if distance < minD:
                    minD = distance
                    minClusterIndex = j

            tempCluster = self.clusters[minClusterIndex]
            tempCluster.clusterPoints.append(self.dataPoints[i])

    #Runs until there has been no change in cluster centers
    def reCluster(self):
        changed = True
        tempMeans = [[0 for i in range(len(self.clusters[0].mean))] for j in range(self.k)]
        for i in range(len(self.clusters) - 1):
            tempMeans[i] = self.clusters[i].mean
        #While there is a difference in the cluter centers from the previous iteration
        while (changed == True):
            #Re assings each data point to the new cluster center
            self.reCenter()
            changed = False
            #Checks to see if there is a difference
            for i in range(len(self.clusters)):
                for j in range(len(self.clusters[i].mean)):
                    if (math.fabs(tempMeans[i][j] - self.clusters[i].mean[j])) > 0.00001:
                        changed = True
                tempMeans[i] = self.clusters[i].mean

    def reCenter(self):
        #for each cluster
        for i in self.clusters:
            #checks to see if a cluster is empty
            if (len(i.clusterPoints) != 0):
                #Recalculates the clusters center
                i.calcCentroid()
            i.clusterPoints = []
        #Re assinges each data point
        self.cluster()


    # Calculates the distance in between two vectors
    def calcDistance(self, d1, d2):
        distance = 0.0
        for i in range(len(d1)):
            # adds the square of the difference of each variable in the data point
            distance += math.pow((d1[i] - (d2[i])), 2)
            # returns the Euclidean distance between two vectors
        return math.sqrt(distance)


    def print(self):
        for i in self.clusters:
            print(i.clusterPoints, 'point')
    #Returns the fitness of the clsutered data set
    def getFitness(self):
        data = []
        for cluster in self.clusters:
            data.append(cluster.clusterPoints)
        return(calc.avgSilhouetteFitness(data, self.dataPoints))