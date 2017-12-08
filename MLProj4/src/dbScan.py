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
        self.run()

    def makeDataPoints(self):
        for point in self.data:
            self.dataPoints.append(DataPoint(point))

    def run(self):
        clustNum = 0
        randIndex = int(r.uniform(0, len(self.dataPoints) - 1))
        temp = self.dataPoints
        data = []
        while len(temp) > 1:
            point = temp[randIndex]
            if point.visited == False:
                point.visited = True
                clustNum = self.scan(clustNum, point)
                del temp[randIndex]
                print(len(temp))
            else:
                del temp[randIndex]
                print(len(temp))
            randIndex = int(r.uniform(0, len(temp) - 1))
        for i in range(clustNum):
            self.centers.append(Cluster())
            data.append([])
        for point in self.dataPoints:
            index = point.clusterVal
            if index is not -1:
                self.centers[index].addPoint(point.point)
                self.data[index].append(point)
        if clustNum <= 6:
            print(data)
            graph(data, clustNum)
        else:
            print('change params there are ', clustNum, ' clusters')

    def scan(self, cluster, point):
        toCheck = []
        hadVal = False
        toCheck.append(point)
        while len(toCheck) is not 0:
            potentialCores = self.calcPointsInRegion(toCheck.pop())
            if len(potentialCores) > 0:
                hadVal = True
                for i in potentialCores:
                    i.clusterVal = cluster
                    i.visited = True
                    toCheck.append(i)
        if hadVal:
            return cluster + 1
        else:
            return cluster

    def calcPointsInRegion(self, centerPoint):
        regionPoints = []
        for point in self.dataPoints:
            if dist(point.point, centerPoint.point) < self.epsilon:
                regionPoints.append(point)
        if len(regionPoints) >= self.minPoints:
            return regionPoints
        else:
            centerPoint.visited = True
            return []

