from numpy import random as rand

class Node:
    def __init__(self, dataSize):
        self.weights = []
        for i in range (dataSize):
            val = rand.uniform(0,1)
            self.weights.append(val)
        self.normalizeWeights()
    def updateWeights(self, point, learningRate):
        for i in range(len(self.weights)):
            self.weights[i] += learningRate * point[i]
        self.normalizeWeights()
    def getActive(self, dataP):
        sum = 0
        for att in range(len(dataP)):
            sum += dataP[att] * self.weights[att]
        return sum
    def normalizeWeights(self):
        weightSum = sum(self.weights)
        for att in range(len(self.weights)):
            self.weights[att] = self.weights[att] / float(weightSum)