from KMeans.cluster import Cluster
from Competetive.node import Node
class Network:
    def __init__(self,data, numClusters, learningRate):
        self.learningRate = learningRate
        self.data = data
        self.numClusters = numClusters
        self.inputLayer = []
        self.outputLayer = []
        # holds the clusters, in each cluster there are the data points
        self.clusters = []

    def makeNet(self):
        for i in range(self.numClusters):
            self.outputLayer.append(Node(len(self.data[0])))
            print(self.outputLayer[i].weights)
            self.clusters.append(Cluster())
            self.clusters[i].clusterPoints.pop()

    def train(self):
        for point in self.data:
            activs = []
            for Node in self.outputLayer:
                activs.append(Node.getActive(point))
            index = activs.index(max(activs))
            p1 = point
            self.clusters[index].addPoint(p1)
            self.outputLayer[activs.index(max(activs))].updateWeights(point, self.learningRate)
            activs.clear()
    def feedIn(self, data):
        for point in data:
            activs = []
            for Node in self.outputLayer:
                activs.append(Node.getActive(point))
            index = activs.index(max(activs))
            p1 = point
            self.clusters[index].addPoint(p1)
            activs.clear()


    def print(self):
        for clust in self.clusters:
            print(clust.clusterPoints)
    def getFitness(self):
        sum = 0
        count = 0
        for cluster in self.clusters:
            if len(cluster.clusterPoints) == 0:
                pass
            else:
                count += 1
                sum += cluster.calcFitness()
        return (sum / count)
