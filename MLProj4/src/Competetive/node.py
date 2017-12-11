from numpy import random as rand
#A node class to be used in the competetive learning neural network
class Node:
    def __init__(self, dataSize):
        #Weight values
        self.weights = []
        #Initializes random weight values
        for i in range (dataSize):
            val = rand.uniform(0,1)
            self.weights.append(val)
        self.normalizeWeights()
    #Updates the weight values
    def updateWeights(self, point, learningRate):
        for i in range(len(self.weights)):
            self.weights[i] += learningRate * point[i]
        self.normalizeWeights()
    #Calculates the sum of w_i * x_i to be used as the output
    def getActive(self, dataP):
        sum = 0
        for att in range(len(dataP)):
            sum += dataP[att] * self.weights[att]
        return sum
    #Normalizes the weight values
    def normalizeWeights(self):
        weightSum = sum(self.weights)
        for att in range(len(self.weights)):
            self.weights[att] = self.weights[att] / float(weightSum)