import math
from calculations import calcDistance
class Cluster:

    def __init__(self, mean = 0):
        
        self.mean = mean
        self.clusterPoints = []
    #adds a data point to the closet mean
    def addPoint(self, point):
        self.clusterPoints.append(point)
    #Calculates the average of all the data points in the cluster
    def calcCentroid(self):
        sum = [0] * len(self.clusterPoints[0])
        for i in range(len(self.clusterPoints)):
            temp = self.clusterPoints[i]
            if len(temp) != 0:
                for j in range(len(temp)):
                    sum[j] += temp[j]
        for k in range(len(sum)):
            sum[k] /= float(len(self.clusterPoints))

        self.mean = sum
        #self.clusterPoints = []
    def getMean(self):
        return self.mean
    def calcFitness(self):
        self.calcCentroid()
        sum = 0
        if(len(self.clusterPoints) == 0):
            print("empty cluster")
            return 0
        else:
            for point in self.clusterPoints:
                sum += calcDistance(point,self.mean)
                return (sum / len(self.clusterPoints))
