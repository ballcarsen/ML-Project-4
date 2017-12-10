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
from dbScan import dbScan

d1 = Data(2)
d1.readData('indians2.txt')
d1.scale()
#print(d1.data)

k = 10
'''

mockData = []
for i in range(500):
    point = []
    for j in range(2):
        val = rand.uniform(0,.3)
        point.append(val)
    mockData.append(point)

    point = []
    for j in range(2):
        val = rand.uniform(.7,1)
        point.append(val)
    mockData.append(point)

    point = []
    val = rand.uniform(0, .3)
    point.append(val)
    val = rand.uniform(.7, 1)
    point.append(val)
    mockData.append(point)

    point = []
    val = rand.uniform(.7, 1)
    point.append(val)
    val = rand.uniform(0, .3)
    point.append(val)
    mockData.append(point)



'''
d1 = Data(2)


d1.getFolds()
mockData = d1.crossValidatedTrain[0]
#print(mockData[0])

#mockData.append(d1.crossValidatedTest[0])
for i in d1.crossValidatedTest[0]:
    print(i)
    mockData.append(i)
#d1 = dbScan(50, .2, mockData)
#print(d1.run())
''''
theData = []
for i in range(5):
    for k in d1.crossValidatedTrain:
        theData.append(k)



dataLength = len(mockData)
dis = [.5, .4, .3, .25, .125]
min = [52, 30, 25, 20 , 15, 10 ,5]
params = []
results = []
for i in range(len(dis)):
    for k in range(len(min)):
        #params.append([[(dataLength / (2 * ((i + 1)* (k  +1))))], [dis[k]]])
        params.append([[min[k]], [dis[i]]])
#print(params[75])

#d1 = dbScan(24, .07, mockData)
#print(d1.run())

def db():
    for i in params:
        print(i)
        d1 = dbScan(i[0][0], i[1][0], mockData)
        outPut = d1.run()
        results.append(outPut)
    for i in range(len(results)):
        print(results[i], params[i])
def net():
    N1 = Network(mockData, k, .005)
    N1.makeNet()
    N1.train()
    print(N1.getFitness())
#for i in range(1, 6):
    #N1.feedIn(d1.crossValidatedTrain[i])
#N1.print()
'''
k1 = KMeans(mockData, k)
k1.cluster()
k1.reCluster()
k1.print()
print(k1.getFitness(), 'fitness')
'''
data1 = []
data2 =[]
for i in range(k):
    data1.append(N1.clusters[i].clusterPoints)
    data2.append(k1.clusters[i].clusterPoints)
calculations.graph(data1,k)
calculations.graph(data2,k)

'''