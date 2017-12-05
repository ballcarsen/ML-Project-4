from numpy import random as rand

class Node:
    def __init__(self, dataSize):
        self.weights = []
        for i in range (dataSize):
            val = rand.uniform(0,1)
            self.weights.append(val)
    def updateWeights(self, point, learningRate):
        for i in range(len(self.weights)):
            self.weights[i] -= learningRate * (point[i] - self.weights[i])
    def getActive(self, dataP):
        sum = 0
        for att in range(len(dataP)):
            sum += dataP[att] * self.weights[att]
        return sum