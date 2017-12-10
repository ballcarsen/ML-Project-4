#energy 7
#indians 2
#HTRU2 2
#seeds 3
#shuttle 5
from Data import Data
import numpy.random as rand
from Competetive.network import Network
from KMeans.KMeans import KMeans
import calculations
from PSO.PSOClusterAlg import PSOClusterAlg


d1 = Data(2)
d1.readData('../seeds.txt')
d1.scale()
d1.getFolds()
data = d1.crossValidatedTrain[0]
for i in d1.crossValidatedTest[0]:
    print(i)
    data.append(i)

'''
mockData = []
for i in range(100):
    point = []
    val = rand.uniform(0,.25)
    point.append(val)
    val = rand.uniform(.75,1)
    point.append(val)
    mockData.append(point)
    point = []
    val = rand.uniform(.75, 1)
    point.append(val)
    val = rand.uniform(0, .25)
    point.append(val)
    mockData.append(point)
    point = []
    val = rand.uniform(.75, 1)
    point.append(val)
    val = rand.uniform(.75, 1)
    point.append(val)
    mockData.append(point)
    point = []
    val = rand.uniform(0, .25)
    point.append(val)
    val = rand.uniform(0, .25)
    point.append(val)
    mockData.append(point)
'''
k = 10


k1 = KMeans(data, k)
k1.cluster()
k1.reCluster()
print("KMeans fitness: ", k1.getFitness())

pso = PSOClusterAlg(data,k,100)

avgFitness = pso.train(30)
bestClusters = pso.getBestClusters()
myData = []
for c in bestClusters:
    myData.append(c.clusterPoints)
calculations.graph(myData,k)

print("PSO fitness: ", avgFitness)




'''
d1 = Data(2)
d1.data = mockData
d1.getFolds()
theData = []
for i in range(5):
    for k in d1.crossValidatedTrain:
        theData.append(k)

N1 = Network(mockData, k, .005)
N1.makeNet()
N1.train()
#for i in range(1, 6):
    #N1.feedIn(d1.crossValidatedTrain[i])
N1.print()

k1 = KMeans(mockData, k)
k1.cluster()
k1.reCluster()
k1.print()

print(N1.getFitness())
print(k1.getFitness())

data1 = []
data2 =[]
for i in range(k):
    data1.append(N1.clusters[i].clusterPoints)
    data2.append(k1.clusters[i].clusterPoints)
calculations.graph(data1,k)
calculations.graph(data2,k)
'''
