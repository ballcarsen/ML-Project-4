from Data import Data
import numpy.random as rand
from Competetive.network import Network
from KMeans.KMeans import KMeans
from PSO.PSOClusterAlg import  PSOClusterAlg
import calculations
from dbScan import dbScan

d1 = Data(2)
d1.readData('seeds.txt')
d1.scale()
d1.getFolds()
data = d1.crossValidatedTrain[0]
for i in d1.crossValidatedTest[0]:
    data.append(i)
k = 20


def runK(data):
    k1 = KMeans(data, k)
    k1.cluster()
    k1.reCluster()
    return([[k1.getFitness()], ['fitness']])


fits = []
for i in range(10):
    fits.append(runK(data))
print(fits)


def runNet(data):

    N1 = Network(data, k, .005)
    N1.makeNet()
    N1.train()
    print(N1.getFitness() , 'fit')

runNet(data)


def runPSO(data):
    pso = PSOClusterAlg(data, k, 50)
    avgFitness = pso.train(20)
    bestClusters = pso.getBestClusters()
    myData = []
    '''
    for c in bestClusters:
        myData.append(c.clusterPoints)
    calculations.graph(myData, k)
    '''
    print("PSO fitness: ", avgFitness)

runPSO(data)
