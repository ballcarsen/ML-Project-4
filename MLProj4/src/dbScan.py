from KMeans.cluster import Cluster
from dataPoint import DataPoint
from calculations import calcDistance as dist
from calculations import graph
import random as r
class dbScan():
    def __init__(self, minPoints, epsilon, data):
        self.minPoints = minPoints
        self.epsilon = epsilon
        self.data = data
        self.dataPoints = []
        self.currentCluster = -1
        self.centers = []
        self.makeDataPoints()
        self.resultNumClust = None

    def makeDataPoints(self):
        for point in self.data:
            self.dataPoints.append(DataPoint(point))

    def run(self):
        toPrint = []
        #Initial cluster is 0
        clustNum = 0
        #Point at index of the random number returned in the array of data points will be the intial point to
        #Check when a new cluster is started
        randIndex = int(r.uniform(0, len(self.dataPoints) - 1))
        #Copies the data points so temp can gradually get smaller without losing track of the dataPoints
        temp = list(self.dataPoints)
        #Once all points have been checked as core points, or deemed invalid to be core points temp will be empty
        #Stoping the algorithm
        while len(temp) > 1:
            # Point at index of the random number returned in the array of data points will be the intial point to
            # Check when a new cluster is started
            point = temp[randIndex]
            #Checks to see if the point has been considered to be a core
            if point.visited == False:
                #Changes that the point has been considered to  be a core
                point.visited = True
                #Calls scan for the random point chosen, and the current cluster number
                #Increments clustNum when scan has finished looking at all possible points to add
                #to the current cluster
                clustNum = self.scan(clustNum, point)
                #Removes the point that was checked from the temp list
                del temp[randIndex]
            #If the point has been visited, and is not a viable option as a core point, removes the point from
            #the temp list
            else:
                del temp[randIndex]
            #Sets the index for the point chosen to a new random number
            randIndex = int(r.uniform(0, len(temp) - 1))

        #Adds a blank cluster object to a list, as well as a blank list to hold the data points
        #after clustering
        for i in range(clustNum + 1):
            self.centers.append(Cluster())
            toPrint.append([])
        #Adds every dataPoint to a cluster object, and adds the value of the data point to the
        #To print array
        clustersUsed = set([])
        noise = False
        numNoisePoints = 0
        for point in self.dataPoints:

            index = point.clusterVal
            clustersUsed.add(index)
            if index is not -1:
                self.centers[index].addPoint(point.point)
                toPrint[index].append(point.point)
            else:
                self.centers[len(self.centers) - 1].addPoint(point.point)
                toPrint[len(toPrint) - 1].append(point.point)
        if len(self.centers) > clustNum:
            noise = True
            numNoisePoints = len(self.centers[len(self.centers) - 1].clusterPoints)
        print(clustersUsed, noise)
        percentNoise = round((numNoisePoints / len(self.dataPoints)) * 100)
        return([[self.getFiness(noise)] , [clustNum], [percentNoise]])

        #Graphing for 2d data
        #if clustNum <= 6:
            #print(toPrint)
            #graph(toPrint, clustNum + 1)
        #else:
            #print('change params there are ', clustNum, ' clusters')
    #Passed the current cluster number, and a point to check as a core
    def scan(self, cluster, point):
        #Holds the points that need to be checked as cores
        toCheck = []
        #Determines if we need to increment clusNum
        hadVal = False
        #Adds the point passed to toCheck
        toCheck.append(point)
        #Until there are no more points to look at as potential core points
        while len(toCheck) is not 0:
            #After a point has been checked to be a core, it returns a list of the points that
            #are within epsilon of the core point
            potentialCores = self.calcPointsInRegion(toCheck.pop())
            #If toCheck return a non empty list, meaning that the point checked was a valid core
            if len(potentialCores) > 0:
                #Becomes true because a cluster has been made
                hadVal = True
                #For every point that was within epsilon of the valid core point
                for i in potentialCores:
                    #Set the cluster value of the point to the current clsuter num
                    i.clusterVal = cluster
                    #Any point within the cluster will not be chosen by run to
                    if i.visited == False:
                        i.visited = True
                        toCheck.append(i)
        #Returns the current cluster index + 1 if scan made a new cluster
        if hadVal:
            return cluster + 1
        #Returns the current cluster number if no cluster was made
        else:
            return cluster

    #After a point has been checked to be a core, it returns a list of the points that
    #are within epsilon of the core point, returns an empy list if the point checked was not a valid core
    def calcPointsInRegion(self, centerPoint):
        regionPoints = []
        for point in self.dataPoints:
            if dist(point.point, centerPoint.point) < self.epsilon and point.clusterVal == -1:
                regionPoints.append(point)
        if len(regionPoints) >= self.minPoints:
            return regionPoints
        else:
            centerPoint.visited = True
            return []

    def getFiness(self, noise):
        sum = 0
        count = 0
        if noise == True:
            self.centers.pop()
        if len(self.centers) == 0:
            self.resultNumClust = count
            return('only noise')
        else:
            for cluster in self.centers:
                sum += cluster.calcFitness()
                count += 1
            self.resultNumClust = count
            return(sum / len(self.centers))

