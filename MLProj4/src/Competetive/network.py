#Imports
from KMeans.cluster import Cluster
from Competetive.node import Node
from calculations import avgSilhouetteFitness as fit
#A competetive neural network to be used for classification
class Network:
    def __init__(self,data, numClusters, learningRate):
        self.learningRate = learningRate
        self.data = data
        self.numClusters = numClusters
        self.inputLayer = []
        self.outputLayer = []
        # holds the clusters, in each cluster there are the data points
        self.clusters = []
    #Creates the outut nodes and a new empty cluster corresponding to each output node
    def makeNet(self):
        for i in range(self.numClusters):
            self.outputLayer.append(Node(len(self.data[0])))
            self.clusters.append(Cluster())
            #self.clusters[i].clusterPoints.pop()
    #Parses thorugh the data set, assinging each data point to a cluster
    def train(self):
        for point in self.data:
            #The activation values returned from each node
            activs = []
            for Node in self.outputLayer:
                activs.append(Node.getActive(point))
            #The index of the maximum activation value, also corresponds to the cluster at which a data point will be
            #Assinged
            index = activs.index(max(activs))
            self.clusters[index].addPoint(point)
            #Updates the weights for the winning output node
            self.outputLayer[activs.index(max(activs))].updateWeights(point, self.learningRate)
            activs.clear()


    def print(self):
        for clust in self.clusters:
            print(clust.clusterPoints)
    #Returns the fitness of the clustered data set
    def getFitness(self):
        sum = 0
        count = 0
        data = []
        for cluster in self.clusters:
            if len(cluster.clusterPoints) == 0:
                pass
            else:
                data.append(cluster.clusterPoints)
        return(fit(data, self.data))

