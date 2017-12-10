from Data import Data
import numpy.random as rand
from Competetive.network import Network
from KMeans.KMeans import KMeans
import calculations
from dbScan import dbScan
d1 = Data(2)
d1.readData('seeds.txt')
d1.scale()
d1.getFolds()
data = d1.crossValidatedTrain[0]
for i in d1.crossValidatedTest[0]:
    print(i)
    data.append(i)
k =100

def runK(data):
    k1 = KMeans(data, k)
    k1.cluster()
    k1.reCluster()
    k1.print()
    print(k1.getFitness(), 'fitness')
#    runK(data)

def runNet(data):

    N1 = Network(data, k, .005)
    N1.makeNet()
    N1.train()
    print(N1.getFitness() , 'fit')
runNet(data)