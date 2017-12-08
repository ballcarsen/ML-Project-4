#energy 7
#indians 2
#HTRU2 2
#seeds 3
#shuttle 5
from Data import Data
import numpy.random as rand
from Competetive.network import Network
from KMeans.kMeans import KMeans
import calculations
from dbScan import dbScan

d1 = Data(2)
d1.readData('HTRU2.txt')
d1.scale()
#print(d1.data)

k = 11

mockData = []
for i in range(20):
    point = []
    for j in range(2):
        val = rand.uniform(0,.5)
        point.append(val)
    mockData.append(point)
    point = []
    for j in range(2):
        val = rand.uniform(.5,1)
        point.append(val)
    mockData.append(point)
d1 = dbScan(3, .05, mockData)
'''
d1 = Data(2)
d1.data = mockData
d1.getFolds()
theData = []
for i in range(5):
    for k in d1.crossValidatedTrain:
        theData.append(k)

N1 = Network(d1.data, k, .5)
N1.makeNet()
N1.train()
#for i in range(1, 6):
    #N1.feedIn(d1.crossValidatedTrain[i])
N1.print()

k1 = KMeans(d1.data, k)
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