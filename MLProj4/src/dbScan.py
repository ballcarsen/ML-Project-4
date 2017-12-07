from KMeans.cluster import Cluster
from dataPoint import DataPoint
from calculations import calcDistance as dist
import random as r
class dbScan():
    def __init__(self, minPoints, epsilon, data):
        self.minPoints = minPoints
        self.epsilon = epsilon
        self.data = data
        self.dataPoints = []
        self.currentCluster = -1
        self.centers = []
    def makeDataPoints(self):
        for point in self.data:
            self.dataPoints.append(DataPoint(point))
    def scan(self):
        self.currentCluster = 0
        #Need some sort of loop
        randIndex = r.random(0, len(self.dataPoints) - 1)
        tempPoint = self.dataPoints[randIndex]
        if tempPoint.visited == False:
            tempPoint.visited = True
            tempPoint.calcPointsInRegion
        else:
            randIndex = r.random(0, len(self.dataPoints) - 1)

    def calcPointsInRegion(self, centerPoint):
        regionPoints = []
        for point in self.dataPoints:
            if dist(point, centerPoint) < self.epsilon:
                regionPoints.append(point)

